import os
from openai import OpenAI  # import open AI client
from dotenv import load_dotenv
from pathlib import Path
from local_tools import *

load_dotenv(Path(__file__).with_name("config.env"))
def connect_openai():
    """
    connect the open ai client with api key and return the client object

    """
    api_key = os.getenv("OPENAI_API_KEY")
    try:
        if(api_key is None):
            raise ValueError("API key is not set. Please set the OPENAI_API_KEY environment variable.")

        client=OpenAI(api_key=api_key)
        return client
    except Exception as e:
        print(f"Error connecting to OpenAI: {e}")
        return None

def connect_openrouter():
    """
    connect the open router client with api key and return client object
    """
    try:
        openrouter_api_key=os.getenv("OPENROUTER_API_KEY")
        if(openroute_api_key is None):
            raise ValueError("Open AI Router Key is not set please set the open router key in enviornment variables")
        client=OpenAI(api_key=openrouter_api_key)
        return client
    except Exception as e:
        print(f'Error connecting with open router: {e}')
        return None



