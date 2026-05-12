from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas import DetectionResponse, Detection
import base64

router = APIRouter()

@router.post("/detect", response_model=DetectionResponse)
async def detect(file: UploadFile = File(...)):
    # Validate the uploaded file is an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    # Read the image bytes
    image_bytes = await file.read()

    # --- Dummy response for now (YOLO goes here in Phase 3) ---
    dummy_detections = [
        Detection(label="person", confidence=0.95, bbox=[100, 150, 300, 500]),
        Detection(label="dog",    confidence=0.87, bbox=[400, 200, 600, 450]),
    ]

    # Return the original image as base64 (annotated version comes in Phase 3)
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    return DetectionResponse(
        detections=dummy_detections,
        count=len(dummy_detections),
        image_base64=image_base64,
    )