import os
from typing import Any, Dict

import openai
from dotenv import load_dotenv

load_dotenv()

class GPT:
  def __init__(self) -> None:
    openai.api_key = os.getenv("OPENAI_API_KEY")
  
  def generate_chat_response(self, prompt: str):
    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                      {"role": "system", "content": "You are a helpful assistant."},
                      {'role': 'user', 'content': prompt}
                    ],
                    stream=True,
                    temperature=0.0,
    )
    return response