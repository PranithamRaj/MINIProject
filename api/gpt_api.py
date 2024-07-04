import os
import streamlit as st
import openai

openai.api_key = os.getenv("OPEN_AI_API_KEY") or st.secrets["OPEN_AI_API_KEY"]["key"]

def fetch_openai_response(prompt):
    response = openai.Completion.create(engine="davinci", prompt=prompt)
    return response.choices[0].text

def set_system_prompt(prompt):
    openai.api_key = os.getenv("OPEN_AI_API_KEY") or st.secrets["OPEN_AI_API_KEY"]["key"]
    return f"System prompt set: {prompt}"
