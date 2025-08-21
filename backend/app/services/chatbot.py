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
        self.embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)
        self.setup_pinecone()
        self.setup_rag_chain()
    
    def setup_pinecone(self):
        pc = Pinecone(api_key=settings.PINECONE_API_KEY)

        if not pc.has_index(settings.PINECONE_INDEX_NAME):
            pc.create_index(
                name=settings.PINECONE_INDEX_NAME,
                dimension=settings.EMBEDDING_DIMENSION,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
        
        self.docsearch = PineconeVectorStore.from_existing_index(
            index_name=settings.PINECONE_INDEX_NAME,
            embedding=self.embeddings
        )
    
    def setup_rag_chain(self):

        system_prompt = settings.PROMPT
        retriever = self.docsearch.as_retriever(search_type="similarity", search_kwargs={"k": settings.MAX_CONTEXT_LENGTH})

        chat_model = ChatGoogleGenerativeAI(model=settings.CHAT_MODEL, temperature=settings.TEMPERATURE)

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        question_answer_chain = create_stuff_documents_chain(chat_model, prompt)
        self.rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    def initialize_vector_store(self, data_path: str = settings.PDF_DATA_PATH):
        documents = load_pdf_documents(data_path)
        filtered_docs = filter_document_metadata(documents)
        text_chunks = split_documents(filtered_docs)

        PineconeVectorStore.from_documents(
            documents=text_chunks,
            index_name=settings.PINECONE_INDEX_NAME,
            embedding=self.embeddings,
        )
    
    def get_answer(self, question: str) -> ChatResponse:
        try:
            response = self.rag_chain.invoke({"input": question})

            source_docs = []
            if "context" in response:
                source_docs = [
                    doc.metadata.get("source", "Unknown")
                    for doc in response.get("context", [])
                ]
            
            return ChatResponse(
                answer=response["answer"],
                source_documents=source_docs
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")
