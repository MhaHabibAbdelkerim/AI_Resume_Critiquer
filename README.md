# 📃 AI Resume Analyzer

___

AI Resume Analyzer is a Streamlit web application that allows users to upload their resumes in PDF format and receive **AI-powered constructive feedback**. The feedback focuses on clarity, relevance to job descriptions, skills presentation, experience presentation, and overall formatting.  

This project leverages the **OpenAI GPT-4o-mini** model to analyze resumes and provide actionable suggestions for improvement.

___

## 🌟 Features

- Upload your resume in PDF format.
- Enter a job description to get **tailored feedback**.
- AI-powered analysis of content, skills, experience, and formatting.
- Clear and structured suggestions to improve your resume.
- Simple and user-friendly Streamlit interface.

___

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/MhaHabibAbdelkerim/AI_Resume_Critiquer.git
```

___ 

## Set up your OpenAI API Key in a .env file

OPENAI_API_KEY="your_openai_api_key_here"

___

## ⚡ Usage:

1) Run the app:
    streamlit run main.py
  
2) Upload your PDF resume and optionally enter a job description.

3) Click Analyze Resume.
   
4) Get AI-powered feedback directly in the app.

## 📁 Project Structure

AI_Resume_Critiquer/
│

├──.env # Contains your OpenAI API key (do NOT push this to GitHub)

├── .env.example # Example environment file without sensitive data

├── .gitignore # To ignore .env and other files

├── main.py # Main Streamlit application

├── requirements.txt # Python dependencies

└── README.md # Project documentation

___ 

## Requirements.txt

* streamlit
* PyPDF2
* openai
* python-dotenv

## Notes

* Make sure your OpenAI API key is valid and stored in the .env file.
* Do not commit your .env file to GitHub to keep your API key secure.
* Only PDF resumes are supported.

## 🧑‍💻 Author
Abdelkerim | GitHub: MhaHabibAbdelkerim
AI and Data Science Student
