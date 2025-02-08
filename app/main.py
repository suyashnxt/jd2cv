from fastapi import FastAPI
from app.routes import resume_routes, ai_routes

app = FastAPI()

# Include Routes
app.include_router(resume_routes.router)
app.include_router(ai_routes.router)

@app.get("/")
async def home():
    return {"message": "Welcome to AI Resume Generator!"}
