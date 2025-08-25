
# Here’s a small RAG example
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Load embeddings & create vector store
embeddings = OpenAIEmbeddings()
db = FAISS.from_texts(["LangChain makes LLM apps modular."], embeddings)

# Build retriever + LLM chain
retriever = db.as_retriever()
llm = ChatOpenAI(model_name="gpt-3.5-turbo")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Ask a question
print(qa.run("What is LangChain?"))
