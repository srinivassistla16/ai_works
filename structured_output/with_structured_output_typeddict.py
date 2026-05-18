from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from models.review import Review

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)
structured_model = model.with_structured_output(Review)

response = structured_model.invoke(
    """
DCB Bank employment Review:
Likes
Nothing at all.worst decision i have ever made

Dislikes
Worst bank i have ever worked with they do forceful resignation.it’s been 3 months only and i was called on multiple review meetings and humiliated infront of my colleagues and asked to resign.they have worst work culture
    """
)

print(response)
