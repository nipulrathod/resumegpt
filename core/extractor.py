import json
import re
from core.prompts import extraction_prompt
from services.llm_handler import ask_llm

def extract_json_from_text(text):
    """
    Extracts the first JSON block from a string, even if wrapped in markdown or has extra text.
    """
    # Remove triple backticks if present
    cleaned_text = text.strip().strip("`")

    # Extract using regex: finds the first {...} block
    match = re.search(r"\{[\s\S]*\}", cleaned_text)
    if match:
        return match.group(0)
    else:
        raise ValueError("No JSON object found in text.")

def extract_info(resume_texts):
    extracted = []

    for resume in resume_texts:
        prompt = extraction_prompt(resume['text'])
        response = ask_llm(prompt)

        print(f"🧠 LLM raw response for {resume['name']}:\n{response}\n")

        try:
            json_str = extract_json_from_text(response)
            data = json.loads(json_str)
            data['file_name'] = resume['name']
            extracted.append(data)
        except Exception as e:
            print(f"❌ JSON parsing failed for {resume['name']}: {e}")
            extracted.append({
                "file_name": resume['name'],
                "error": "Failed to parse JSON response"
            })

    return extracted
