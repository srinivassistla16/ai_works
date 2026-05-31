from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)
response = model.invoke("Please explain the use cases where MongDB is used with full description of technical flow along with pictorial view")
print(response.content[0].get("text"))