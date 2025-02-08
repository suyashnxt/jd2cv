import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

def optimize_resume(resume_text: str, job_description: str):
    """
    Uses Google Gemini AI to optimize a resume for a job description.
    """
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    Improve this resume for the following job description:
    
    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Optimized Resume:
    """

    response = model.generate_content(prompt)

    return response.text if response.text else "Error: No response from AI"
