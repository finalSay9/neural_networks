from fastapi import FastAPI
from app.routers import ocr

app = FastAPI(title="OCR Learning App")
app.include_router(ocr.router, prefix="/ocr")

@app.get("/")
def health_check():
    return {"status": "ok"}