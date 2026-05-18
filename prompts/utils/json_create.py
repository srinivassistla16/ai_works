
from langchain_core.prompts import PromptTemplate
from langchain_core.load import dump
template = PromptTemplate(
    template= """
    Describe {character_input} character in Indian Mythology {mythology_input} in {no_of_lines_input}  sentences
    """,
     input_variables=['character_input', 'mythology_input','no_of_lines_input']
)
template.save("Prompts/Utils/mythology_template_file.json")