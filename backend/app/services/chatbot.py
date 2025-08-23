from fastapi import HTTPException
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from pinecone import Pinecone, ServerlessSpec
from ..core.config import settings
from ..models.chat import ChatResponse
from ..utils.documents import load_pdf_documents, filter_document_metadata, split_documents

class MedicalChatbot:
    def __init__(self):
        """
        Initialize the chatbot:
        - Load embeddings model for vectorization.
        - Set up Pinecone vector database connection.
        - Build the Retrieval-Augmented Generation (RAG) chain.
        """
        self.embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)
        self.setup_pinecone()
        self.setup_rag_chain()
    
    def setup_pinecone(self):
        """
        Configure Pinecone vector database:
        - Connect to Pinecone with API key.
        - Create index if it does not exist.
        - Attach HuggingFace embeddings to the existing Pinecone index.
        """
        pinecone = Pinecone(api_key=settings.PINECONE_API_KEY)
        # Create Pinecone index if not already present
        if not pinecone.has_index(settings.PINECONE_INDEX_NAME):
            pinecone.create_index(
                name=settings.PINECONE_INDEX_NAME,
                dimension=settings.EMBEDDING_DIMENSION,
                metric="cosine",  # Cosine similarity for embeddings
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
        # Connect to the existing index for retrieval
        self.docsearch = PineconeVectorStore.from_existing_index(
            index_name=settings.PINECONE_INDEX_NAME,
            embedding=self.embeddings
        )
    
    def setup_rag_chain(self):
        """
        Build the Retrieval-Augmented Generation (RAG) pipeline:
        - Configure retriever to fetch relevant documents from Pinecone.
        - Load ChatGoogleGenerativeAI (Gemini) model as the LLM.
        - Define prompt template with system and human roles.
        - Create a chain that combines retrieval with document-based QA.
        """
        system_prompt = settings.PROMPT
        # Retriever: fetch top-k most relevant documents
        retriever = self.docsearch.as_retriever(
            search_type="similarity",
            search_kwargs={"k": settings.MAX_CONTEXT_LENGTH}
        )
        # Chat model (Google Gemini API)
        chat_model = ChatGoogleGenerativeAI(
            model=settings.CHAT_MODEL,
            temperature=settings.TEMPERATURE
        )
        # Prompt template: system + user input
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])
        # QA chain: Stuff retrieved documents into LLM prompt
        question_answer_chain = create_stuff_documents_chain(chat_model, prompt)
        # Final RAG pipeline: retrieval + QA
        self.rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    def initialize_vector_store(self, data_path: str = settings.PDF_DATA_PATH):
        """
        Load and preprocess documents, then insert them into Pinecone:
        - Load PDF files.
        - Filter metadata (clean up titles, sources, etc.).
        - Split documents into smaller chunks for better retrieval.
        - Push processed documents into Pinecone vector store.
        """
        documents = load_pdf_documents(data_path)
        filtered_docs = filter_document_metadata(documents)
        text_chunks = split_documents(filtered_docs)
        # Store preprocessed chunks in Pinecone
        PineconeVectorStore.from_documents(
            documents=text_chunks,
            index_name=settings.PINECONE_INDEX_NAME,
            embedding=self.embeddings,
        )

    def get_answer(self, question: str) -> ChatResponse:
        """
        Generate an answer for a user query:
        - Pass question to RAG pipeline.
        - Collect the LLM's response and supporting source documents.
        - Return result wrapped in ChatResponse model.
        """
        try:
            # Run retrieval + generation chain
            response = self.rag_chain.invoke({"input": question})
            # Collect sources if available
            source_docs = []
            if "context" in response:
                source_docs = [
                    doc.metadata.get("source", "Unknown")
                    for doc in response.get("context", [])
                ]
            # Wrap response in ChatResponse dataclass
            return ChatResponse(
                answer=response["answer"],
                # source_documents=source_docs
            )
        except Exception as e:
            # Handle unexpected errors gracefully
            raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")
