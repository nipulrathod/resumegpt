from core.prompts import extraction_prompt
from services.llm_handler import ask_llm
import json

def extract_info(resume_texts):
    extracted = []
    for resume in resume_texts:
        prompt = extraction_prompt(resume['text'])
        response = ask_llm(prompt)
        try:
            data = json.loads(response)
            data['file_name'] = resume['name']
            extracted.append(data)
        except:
            extracted.append({"file_name": resume['name'], "error": "Failed to parse"})
    return extracted