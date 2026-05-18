from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
# step1 prompt
prompt1 = PromptTemplate(
    template = "Details of 5 tourrist attractions in {city}",
    input_variables=["city"]
)

prompt2 = PromptTemplate(
    template = "Summarize the Names of tourrist attractions from the details {details}",
    input_variables=["details"]
)

#model
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)

#parser
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
response = chain.invoke({
    "city" : "Bangalore"
})

print(response)

chain.get_graph().print_ascii()