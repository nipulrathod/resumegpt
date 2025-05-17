import json
from core.prompts import query_prompt
from services.llm_handler import ask_llm

def filter_resumes(user_query, resume_data):
    data_str = json.dumps(resume_data, indent=2)
    prompt = query_prompt(user_query, data_str)
    response = ask_llm(prompt)
    return response.split("\n")