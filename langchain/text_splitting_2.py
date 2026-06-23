from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter


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

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separators=["\n\n", "\n", "(?<=\. )", " ", ""]
)
str_lst = r_splitter.split_text(three_pages)
print("Total number of chunks: ", len(str_lst))
for str in str_lst:
    print(str)
    print("------------------------------------------------------------")
   
  



