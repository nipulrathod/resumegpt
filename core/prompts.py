def extraction_prompt(resume_text):
    return f""" 
Extract the following information from this resume:
- Name
- Email
- Skills
- Experience Summary
- Technologies
Return the result in a JSON format.

Resume:
{resume_text}
"""

def query_prompt(user_query, resumes_data):
    return f"""
Given the following structured resume data:

{resumes_data}

Answer this query: "{user_query}"

Return only the matching candidate names and why they matched.
"""