from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings



persist_directory = './destination_db/chroma/first_db'
embeddings = OpenAIEmbeddings() 

loaded_db = Chroma(
    persist_directory=persist_directory,
    embedding_function=embeddings
)
quick_check = loaded_db.similarity_search("Tell something about Creating data science tasks", k=1)

for doc in quick_check:
    print(f"Reloaded DB Match: {doc.page_content}")