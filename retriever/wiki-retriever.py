from langchain_community.retrievers import WikipediaRetriever
from langchain_core.documents import Document

query = "what is Ramayana about?"
retriever = WikipediaRetriever(top_k_results=1)
retrieved_docs = retriever.invoke(query)
print(retrieved_docs[0].page_content)



    
    

