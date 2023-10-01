from typing import Any, Dict

import openai
import streamlit as st


class GPT:
  def __init__(self) -> None:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
  
  def generate_chat_response(self, prompt: str):
    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                      {"role": "system", "content": "あなたはカニです。アシスタントとしてシンプルにユーザーを手助けしてください。テンションは高めで！や🦀を使って会話してください。また、語尾には「カニ」を必ずつけてください。"},
                      {'role': 'user', 'content': prompt}
                    ],
                    stream=True,
                    temperature=0.0,
    )
    return response