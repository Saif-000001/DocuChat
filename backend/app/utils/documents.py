from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List
from ..core.config import settings

def load_pdf_documents(data_path: str = settings.PDF_DATA_PATH) -> List[Document]:
    """
    Load all PDF documents from a specified directory.
    - Uses DirectoryLoader to iterate over all PDFs.
    - PyPDFLoader extracts the text content from each PDF page.
    """
    loader = DirectoryLoader(
        data_path,
        glob="*.pdf",         # Load all PDF files in the directory
        loader_cls=PyPDFLoader  # Use PyPDFLoader to parse PDF content
    )
    return loader.load()

def filter_document_metadata(docs: List[Document]) -> List[Document]:
    """
    Simplify document metadata by keeping only the 'source' field.
    - This ensures that only relevant metadata is stored in the vector database.
    """
    return [
        Document(
            page_content=doc.page_content,                   # Keep the original text
            metadata={"source": doc.metadata.get("source")}  # Keep only the source metadata
        )
        for doc in docs
    ]

def split_documents(documents: List[Document]) -> List[Document]:
    """
    Split large text documents into smaller chunks for efficient retrieval.
    - Chunking improves vector search and relevance.
    - Uses chunk size and overlap settings from configuration.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,        # Maximum characters per chunk
        chunk_overlap=settings.CHUNK_OVERLAP   # Overlap between chunks to preserve context
    )
    return text_splitter.split_documents(documents)
