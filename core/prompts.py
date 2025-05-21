def extraction_prompt(resume_text):
    return f""" 
You are an information extractor.

Extract the following information from this resume in **valid JSON only**:
- Name
- Email
- Education: A list of objects containing:
    - Degree
    - Institution
    - Year (if available)
- Skills
- Experience Summary
- Technologies

⚠️ Do not include any commentary, explanation, or notes — return only the JSON.

Resume:
{resume_text}
"""

def query_prompt(user_query, resumes_data):
    return f"""
Given the following structured resume data:

{resumes_data}

Answer this query: "{user_query}"

Return only the matching candidate names and a short reason why they matched (like skills or experience match).
Avoid showing raw JSON or unrelated fields.
"""