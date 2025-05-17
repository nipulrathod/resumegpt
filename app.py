import streamlit as st
from services.pdf_parser import parse_pdfs
from services.llm_handler import ask_llm
from core.extractor import extract_info
from core.query_engine import filter_resumes

st.set_page_config(page_title="ResumeGPT")
st.title("📄 ResumeGPT")

uploaded_files = st.file_uploader("Upload Resumes (PDFs)", type=["pdf"], accept_multiple_files=True)

query = st.text_input("Enter your query (e.g. 'Who has experience in Python and SQL?')")

if st.button("Run Query"):
    if uploaded_files and query:
        resume_texts = parse_pdfs(uploaded_files)
        structured_data = extract_info(resume_texts)
        results = filter_resumes(query, structured_data)
        st.success("Query executed!")
        
        for result in results:
            st.write(result)
            
    else:
        st.warning("Please upload resumes and enter a query.")