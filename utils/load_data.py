import os, sys, dotenv
import langchain
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community import document_loaders
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY')

file_path = "/home/biniyam/Prompt-Generation/data/1706.03762.pdf"
loader = PyPDFLoader(file_path)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500)
doc = text_splitter.split_documents(loader.load_and_split())



def embed_context(doc):
    vectorstore = Chroma.from_documents(doc, OpenAIEmbeddings())
    persist_directory = 'db'
    embedding = OpenAIEmbeddings()

def retriever(query, vectorstore, k):
    retriever = vectorstore.as_retriever(search_kwargs={'k': k})
    documents = retriever.get_relevant_documents(query)
    return documents


