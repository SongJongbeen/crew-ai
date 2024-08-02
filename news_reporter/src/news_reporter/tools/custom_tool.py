import requests
import os
from crewai_tools import BaseTool
from dotenv import load_dotenv
load_dotenv()


class GlobalNewsResearchTool(BaseTool):
    name: str = "Global News Research Tool"
    description: str = (
        "This tool allows you to research global news from all around the world, "
        "you can use it to get the latest news in a json format."
    )

    def _run(self):
        url = ('https://api.currentsapi.services/v1/latest-news?'
        'language=us&'
        f'apiKey={os.getenv("CURRENTS_API_KEY")}')
        response = requests.get(url)
        return response.json()

class LocalNewsResearchTool(BaseTool):
    name: str = "Local News Research Tool"
    description: str = (
        "This tool allows you to research local news from Republic of Korea, "
        "you can use it to get the latest news in a json format."
    )

    def _run(self):
        url = ('https://api.currentsapi.services/v1/latest-news?'
        'language=ko&'
        f'apiKey={os.getenv("CURRENTS_API_KEY")}')
        response = requests.get(url)
        return response.json()