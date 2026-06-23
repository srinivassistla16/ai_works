from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

# Initialize the loader with your PDF file path
loader = PyPDFLoader(file_path="./source_docs/LLMs.pdf")

# Load documents synchronously
docs = loader.load()

three_pages = ""
i = 0
for doc in docs:
    if i <= 5:
        three_pages = three_pages + str(doc.page_content)
    else:
        break
    i = i + 1

print(three_pages)


#model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.1)
#response = model.invoke("Please explain the use cases where MongDB is used with full description of technical flow along with pictorial view")
#print(response.content[0].get("text"))