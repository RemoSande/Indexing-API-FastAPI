from dotenv import find_dotenv, load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
import requests

load_dotenv(find_dotenv())

embeddings = OpenAIEmbeddings()

loader = TextLoader('./FAQ/japanese.txt')
docs = loader.load()

'''   Args:
        file_path: Path to the file to load.

        encoding: File encoding to use. If `None`, the file will be loaded
        with the default system encoding.

        autodetect_encoding: Whether to try to autodetect the file encoding
            if the specified encoding fails.

'''

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=20,
)

documents = text_splitter.split_documents(docs)
docs_data = [doc.dict() for doc in documents]

print(docs_data[0:4])

url = "http://localhost:8001/index?cleanup=incremental"
response = requests.post(url, json=docs_data)
print(response.json())
