from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
# for text splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter
# vecor store and embeddings
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


load_dotenv()

# Initialize the loader with your PDF file path
loader = PyPDFLoader(file_path="./source_docs/LLMs.pdf")

# Load documents synchronously
docs = loader.load()



r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)
docs_lst = r_splitter.split_documents(docs)
'''
print("Total number of chunks: ", len(str_lst))
for str in str_lst:
    print(str)
    print("------------------------------------------------------------")
'''
# Initialize the embedding model
embeddings = OpenAIEmbeddings() 
# Generate embeddings
for doc in docs_lst:
    embeddings.embed_query(doc.page_content)  

persist_directory = './destination_db/chroma/first_db'

vectordb = Chroma.from_documents(
    documents=docs_lst,
    embedding=embeddings,
    persist_directory=persist_directory
)
print("Vector store created successfully.")

