from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

model_name = "text-embedding-3-small"
embedding_model = OpenAIEmbeddings(model=model_name, dimensions=30)

documents = [
    "Rama is hero in Ramayana",
    "Sita is wife of Rama",
    "Hanuman is devotee of Rama",
    "Lakshmana is brother of Rama"
]
text = "Rama's brother is Lakshmana"
doc_embeddings = embedding_model.embed_documents(documents)
text_embedding = embedding_model.embed_query(text)

similarities = cosine_similarity([text_embedding], doc_embeddings)
print(similarities)
most_similar_doc_index = np.argmax(similarities)

print(f"Most similar document: {documents[most_similar_doc_index]}")
