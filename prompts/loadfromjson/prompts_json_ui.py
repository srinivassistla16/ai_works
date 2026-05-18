from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)

st.header("Mythology Character Description")

character_input = st.selectbox('Character Name', ['Duryodhan', 'Sakuni', 'Lakshmana', 'Satya Bhama'])
mythology_input = st.selectbox("Mythology", ["Ramayan", "Maha Bharat", 'Bhagavatham'])
no_of_lines_input = st.selectbox("No of Lines", [1,2,3])

template = load_prompt("Prompts/Utils/mythology_template_file.json")

prompt = template.invoke(
    {
        "character_input" : character_input,
        "mythology_input" : mythology_input,
        "no_of_lines_input": no_of_lines_input
    }
)
if st.button("Describe"):
    response = model.invoke(prompt)
    st.write(response.content[0].get("text"))


