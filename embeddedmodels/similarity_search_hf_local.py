from sentence_transformers import SentenceTransformer

model = SentenceTransformer(model_name_or_path="sentence-transformers/all-MiniLM-L6-v2")
text = "Rama's brother is Lakshmana"
documents = [
    "Rama is hero in Ramayana",
    "Sita is wife of Rama",
    "Hanuman is devotee of Rama",
    "Lakshmana is brother of Rama"
]
text = "Rama's brother is Lakshmana"
vector_source = model.encode(documents)
vector_search_txt = model.encode(text)
print(str(vector_source))
print("OKKKK")
print(str(vector_search_txt))