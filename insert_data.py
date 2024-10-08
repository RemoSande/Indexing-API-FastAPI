from dotenv import find_dotenv, load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
import requests

load_dotenv(find_dotenv())

embeddings = OpenAIEmbeddings()

loader = DirectoryLoader('./FAQ', glob="**/*.txt", loader_cls=TextLoader)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=20,
)

documents = text_splitter.split_documents(docs)
docs_data = [doc.dict() for doc in documents]

url = "http://localhost:8001/index?cleanup=incremental"
response = requests.post(url, json=docs_data)
print(response.json())

