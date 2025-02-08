from fastapi import APIRouter, UploadFile, File
from app.services.resume_parser import extract_text_from_resume

router = APIRouter()

@router.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    text = extract_text_from_resume(file)
    return {"extracted_text": text}
