from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
# gpt-4.1-nano
load_dotenv()
model = ChatOpenAI(model="gpt-4.1-nano", temperature=1.5)
response = model.invoke("Write 5 lines summary notes of Andhra Pradesh polytics")
print(response.content)