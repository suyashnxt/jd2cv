from fastapi import APIRouter, UploadFile, File
from app.services.resume_parser import extract_text_from_resume
from app.services.ai_optimizer import optimize_resume

router = APIRouter()

@router.post("/process_resume/")
async def process_resume(file: UploadFile = File(...), job_description: str = "Default JD"):
    """
    Uploads a resume, extracts text, and optimizes it using DeepSeek AI.
    """
    resume_text = extract_text_from_resume(file)  # Auto-extract resume text
    optimized_text = optimize_resume(resume_text, job_description)  # AI Optimization
    return {"optimized_resume": optimized_text}
