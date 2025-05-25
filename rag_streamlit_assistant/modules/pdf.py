# PDF loading and splitting logic
from langchain.document_loaders import PyPDFLoader

def load_pdf(file):
    loader = PyPDFLoader(file)
    docs = loader.load_and_split()
    return docs
