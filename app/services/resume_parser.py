import pdfminer.high_level
import docx2txt
import fitz  # PyMuPDF
from fastapi import UploadFile

def extract_text_from_resume(file: UploadFile):
    """
    Extracts text from a resume (PDF/DOCX).
    """
    try:
        file_content = file.file.read()  # Read file into memory
        file.file.seek(0)  # Reset file pointer after reading

        if file.filename.endswith(".pdf"):
            # pdfminer requires a file path or file-like object, so we use a BytesIO object
            from io import BytesIO
            pdf_file = BytesIO(file_content)
            text = pdfminer.high_level.extract_text(pdf_file)

            if not text.strip():  # If text extraction fails, use PyMuPDF
                pdf_document = fitz.open(stream=file_content, filetype="pdf")
                text = "\n".join(page.get_text() for page in pdf_document)
        
        elif file.filename.endswith(".docx"):
            from io import BytesIO
            doc_file = BytesIO(file_content)
            text = docx2txt.process(doc_file)
        
        else:
            return "Unsupported file format. Please upload a PDF or DOCX."

        return text

    except Exception as e:
        print(f"Error extracting text: {e}")
        return f"Error: {e}"
