AI-Resume-Analyser-using-API

AI powered Resume Analyser built with Streamlit and OpenAI. Upload a PDF or TXT resume, optionally specify a target job role, and receive structured, actionable feedback to improve content, technical skills, experience descriptions, and job alignment.

Features
Upload resumes in PDF or TXT format
AI-powered resume analysis using OpenAI
Optional analysis based on a target job role
Actionable recommendations for improving your resume
Feedback focused on:

Content clarity and impact

Technical skills presentation

Work experience descriptions

Alignment with the target job role

Simple and user-friendly Streamlit interface

API key loaded securely using environment variables

Streamlit Page Once Completed
<img width="1920" height="1080" alt="Screenshot (1130)" src="https://github.com/user-attachments/assets/8bbc7c96-284e-44af-b2e9-502cec7b903f" />
Clone the Repository
git clone https://github.com/jaishcodes/AI-Resume-Analyser-using-API.git

cd AI-Resume-Analyser-using-API

Configure Your API Key

Create a .env file in the project directory and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here


Note: Never share your API key publicly or upload your .env file to GitHub.

Run the Application
uv run streamlit run AI_Resume_Analyser.py

How to Use
Open the application.
Upload your resume in PDF or TXT format.
Enter the job role you're targeting, such as:
Software Engineer
Data Analyst
Click on Analyse Resume.
Review the AI-generated feedback.
Use the recommendations to improve your resume.
Technologies Used
Python
Streamlit
OpenAI API
PyPDF2
python-dotenv
uv

Author
Jaishwanth Arun
GitHub: https://github.com/jaishcodes
