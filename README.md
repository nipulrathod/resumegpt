# 📄 ResumeGPT

**ResumeGPT** is a powerful AI-driven Streamlit web app that allows users to upload multiple resume PDFs and perform **natural language queries** to filter and search candidates based on their skills, technologies, or experience. It uses **Groq API** (LLM backend) to parse and understand resumes intelligently.

---

## 🚀 Features

- ✅ Upload and parse multiple resume PDFs.
- 🧠 Extract structured data: Name, Email, Skills, Experience Summary, Technologies.
- 🔍 Ask natural language queries (e.g. _"Who knows Python and worked with SQL?"_).
- 🤖 AI-powered filtering using LLM (Groq/OpenAI).
- ⚡ Built using **Streamlit**, **Groq API**, **PyPDF2**, and **dotenv**.

---

## 🔧 Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/ResumeGPT.git
cd ResumeGPT
```
### 2. Create and activate a virtual environment (optional but recommended)

```
# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install required dependencies

```
pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a `.env` file in the root directory and add your API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

### ▶️ Usage

Run the app using Streamlit:

```
streamlit run app.py
```

### How to Use
📤 Upload one or more resume PDF files.

🗣️ Enter a natural language query (e.g., "Who has worked with Django and React?").

✅ View filtered candidates and reasons for the match.

### 📦 Requirements
Python 3.8+
Streamlit
PyPDF2
python-dotenv
Groq SDK (via OpenAI-compatible library)
