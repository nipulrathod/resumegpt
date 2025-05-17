import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



model = genai.GenerativeModel("models/gemini-1.5-pro")

def ask_llm(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text.strip()
