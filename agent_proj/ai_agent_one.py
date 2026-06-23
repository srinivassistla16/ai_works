from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent,agent_executor
from langchain import hub
from dotenv import load_dotenv

load_dotenv()


#model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)
#print(model.invoke("Please explain the use cases where MongDB is used with full description of technical flow along with pictorial view").content[0].get("text"))
search_tools = DuckDuckGoSearchRun()
#response = search_tools.invoke("what is the BSE Sensex  Points today?")
#print(response)
