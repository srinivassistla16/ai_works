from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
result = llm.invoke("is it wise to close down my SIP in the current scenario as on May 2026 ?")
print(result)