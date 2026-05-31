from pseudo_llm import PseudoLLM
from pseudo_prompt import PseudoPrompt


llm = PseudoLLM()
res = llm.predict("What is the capital of France?")
print(res)

template = PseudoPrompt(
    "template: write 5 important places in  {city}",
    "input_variables = ['city']"
)

prompt_text = template.format({"city": "Paris"})

llm.predict(prompt_text)
