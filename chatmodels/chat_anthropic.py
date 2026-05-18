from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-sonnet-4-6", temperature=1.5)
response = model.invoke("Write 5 lines summary notes of Andhra Pradesh polytics")
print(response.content)