from fastapi import APIRouter, UploadFile, File
import numpy as np
import cv2

router = APIRouter()

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # TODO: call your preprocessing pipeline here
    # TODO: call your OCR engine here
    # TODO: call postprocessing/regex extraction here

    return {
        "filename": file.filename,
        "shape": img.shape,   # just proving the image loaded correctly
        "text": "NOT_IMPLEMENTED_YET"
    }