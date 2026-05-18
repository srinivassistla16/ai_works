from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation"
    )



model = ChatHuggingFace(llm=llm)
response = model.invoke("what is capital of Japan ?")
print(response.content)
