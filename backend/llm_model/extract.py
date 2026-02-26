from groq import Groq
import os, json

import logging

from backend.agent.logic import Agent_logic
from backend.llm_model.prompt import prompt_engine

logger = logging.getLogger(__name__)

client = Groq(api_key = os.getenv('Groq_Api_key'))

def extract_llm(raw_text : str) -> dict:

    prompt = prompt_engine(raw_text)

    response = client.chat.completion.create(
        model = 'llama-3.1-8b-instant',
        message = [
            {'role' : 'system', 'content' : 'your an extraction engine, extract the required details from user text'},
        {'role' : 'user', 'content' : prompt}],
        temperature = 0,
        max_completion_token = 256
    )

    content = response.choice[0].message.content.strip()
    try :
        parsed = json.load(content)
    except json.JSONDecodeError :
         logger.error('llm model failed to extract an details from input')
         parsed = {
        "client_name": None,
        "topic": None,
        "action": None
        }

         


    
    return parsed

