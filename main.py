#Import the necessary libraries
import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

# Set up the Streamlit app
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📃", layout="centered")

# App title and description
st.title("📃 AI Resume Analyzer")
st.markdown("Upload your resume in PDF format, and get AI-powered feedback to improve it!")

# Get OpenAI API key from environment variables
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

# File uploader and job description input
upload_file = st.file_uploader("Choose a PDF file to analyze", type="pdf")
job_description = st.text_input("Enter the job description (optional):")

# Analyze button
analyze = st.button("Analyze Resume")


#Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to extract text based on file type
def extract_text_from_file(upload_file):
    if upload_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(upload_file.read()))
    return upload_file.read().decode("utf-8")


# Analyze the resume when the button is clicked
if analyze and upload_file:
    try: 
        file_content = extract_text_from_file(upload_file)

        if not file_content.strip():
            st.error("The uploaded PDF file is empty or could not be read.")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback on how to improve it.
        Focus on clarity, relevance to the job description, formatting, and overall presentation.
        Focus on these main areas:
        1. Content quality, impact, and clarity.
        2. Relevance to the job description.
        3. Skills presentation (how the user talked about their skills)
        4. Experience presentation (how the user talked about their experience)
        5. Formatting and structure.
        6. Specific improvements for {job_description if job_description else 'general job applications'}


        Resume content:
        {file_content}

        Please provide your feedback in a clear and structured manner with specific suggestions for improvement. """

        client= OpenAI(api_key=OPEN_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer with many years of experience in reqruitment and career coaching."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7,

        )

        # Display the feedback
        st.markdown("### Feedback")
        st.markdown(response.choices[0].message.content)
    
    # Handle exceptions and display error messages
    except Exception as e:
        st.error(f"An error occurred during analysis: {e}")
        








