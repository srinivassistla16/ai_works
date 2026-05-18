from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, chain

load_dotenv()


#model
model_gemini = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)
#parser
parser = StrOutputParser()

# step1 prompt
prompt_story = PromptTemplate(
    template = " Please provide notes on Ramayana story",
    input_variables=[]
)

story_chain = prompt_story | model_gemini | parser

story_text = story_chain.invoke({
   
})

prompt1 = PromptTemplate( 
    template="Generate a short Summary on the notes {story_text} in 5 lines",
    input_variables= ["story_text"]
)


prompt2 = PromptTemplate(
    template = "Generate 5 muliple choice questions from the  text {story_text}",
    input_variables=["story"]
)

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation"
    )

model_huggingface = ChatHuggingFace(llm=llm)

paralle_chain = RunnableParallel(
    {
        "notes": prompt1 | model_gemini | parser,
        "quiz": prompt2 | model_huggingface | parser
    }
)
  
prompt3 = PromptTemplate(
    template = "Merge the notes into single document \n Notes: {notes} \n Quiz: {quiz}",
    input_variables=["notes","quiz"]
)

merge_chain = prompt3 | model_gemini | parser

chain = paralle_chain | merge_chain
response = chain.invoke({
    "story_text" : story_text
})