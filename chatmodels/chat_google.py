from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)
response = model.invoke("which is bigger number among 2 and 4 ?")
print(response.content[0].get("text"))