# Ref: https://www.youtube.com/watch?v=HdcLE8JuMrA&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=5

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os

os.environ['HF_HOME'] = "D:/aSrinivas/python-essentials/huggingface_cache"

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v0.6",
    task="text-generation",
    pipeline_kwargs= dict(
        temperature = 0.7,
        max_new_tokens = 200
    )
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("What is capital of France")
print(response.content)


