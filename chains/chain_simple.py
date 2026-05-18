from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
# step1 prompt
prompt = PromptTemplate(
    template = "Write 2 tourrist attractions in {city}",
    input_variables=["city"]
)

#model
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)

#parser
parser = StrOutputParser()

chain = prompt | model | parser
response = chain.invoke({
    "city" : "Bangalore"
})

print(response)

chain.get_graph().print_ascii()