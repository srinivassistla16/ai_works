from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
documents = [
    "Rama is hero in Ramayana",
    "Sita is wife of Rama",
    "Hanuman is devotee of Rama",
    "Lakshmana is brother of Rama"
]

model_name = "text-embedding-3-small"
embedding_model = OpenAIEmbeddings(model=model_name, dimensions=30)

async def generate_embeddings():
    vec = await embedding_model.aembed_documents(documents)
    print(str(vec))

if (__name__ == "__main__"):
    import asyncio
    asyncio.run(generate_embeddings())  
