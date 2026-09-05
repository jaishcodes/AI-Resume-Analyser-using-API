# Import required libraries
import io
import os
import PyPDF2
import streamlit as st

# OpenAI client and dotenv for loading environment variables
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Streamlit page configuration
st.set_page_config(
    page_title="AI Resume Analyser",
    page_icon="📝"
)

st.title("AI Resume Analyser")
st.markdown("Upload your resume and get AI powered feedback.")

# File uploader
# Allows the user to upload either a PDF or TXT file
uploaded_file = st.file_uploader(
    "Upload your resume (PDF or TXT)",
    type=["pdf", "txt"]
)

# Optional job role input
job_role = st.text_input(
    "Enter the job role that you are targeting (Optional)"
)

# Analyse button
analyse = st.button("Analyse Resume")

# Function to extract text from a PDF
def extract_text_from_pdf(uploaded_file):
    #Reads a PDF file and extracts text from every page.
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    # Loop through every page in the PDF
    for page in pdf_reader.pages:

        # extract_text() is the current PyPDF2 method
        # for extracting text from a page
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

# Function to extract text from either PDF or TXT
def extract_text_from_file(uploaded_file):
    # Determines the file type and extracts its text.
    # Check whether the uploaded file is a PDF
    if uploaded_file.type == "application/pdf":

        # Convert the uploaded file into a BytesIO object
        # so PyPDF2 can read it
        pdf_file = io.BytesIO(uploaded_file.read())

        return extract_text_from_pdf(pdf_file)

    # Otherwise, assume it is a TXT file
    return uploaded_file.read().decode("utf-8")

# Main application logic
# This runs when the user clicks Analyse Resume and has uploaded a file.
if analyse and uploaded_file:

    try:
        # Extract text from the uploaded resume
        file_content = extract_text_from_file(uploaded_file)

        # Make sure the extracted text is not empty
        if not file_content.strip():
            st.error("The uploaded file is empty or no text could be extracted.")
            st.stop()

        # Create the prompt for the AI
        # If the user entered a job role, use it.
        # Otherwise, use "general job application".
        target_role = job_role if job_role else "general job application"

        prompt = f"""
Analyse this resume and provide constructive feedback
that will help the user make improvements.

Focus on the following aspects:

1. Content clarity and impact on the hiring manager
2. Presentation of technical skills
3. Description of work experience
4. Specific improvements for the target job role: {target_role}

Resume content:
{file_content}

Please provide the analysis in a clear and structured format
with specific and actionable recommendations.
"""
        # Check whether the API key exists
        if not OPENAI_API_KEY:
            st.error(
                "OPENAI_API_KEY was not found. "
                "Please add it to your .env file."
            )
            st.stop()

        # Create the OpenAI client
        client = OpenAI(api_key=OPENAI_API_KEY)

        # Send the resume and prompt to the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
          messages=[
                {
                    "role": "system",
                    "content": ("You are an expert resume reviewer with years of experience in HR and recruitment.")},
                {"role": "user", "content": prompt}
            ],

            # Controls how creative/random the response is
            temperature=0.7,

            # Maximum number of tokens in the response
            max_tokens=1000
        )

        # Display the AI response in Streamlit
        st.markdown("### Analysis Results")

        st.markdown(
            response.choices[0].message.content
        )

    # Catch and display any errors
    except Exception as e:
        st.error(f"An error has occurred: {str(e)}")
