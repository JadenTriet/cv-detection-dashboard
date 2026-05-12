from pydantic import BaseModel
from typing import List

class Detection(BaseModel):
    label: str        # e.g. "person", "car", "dog"
    confidence: float # e.g. 0.94 (94% confident)
    bbox: List[float] # bounding box: [x1, y1, x2, y2] in pixels

class DetectionResponse(BaseModel):
    detections: List[Detection]
    count: int
    image_base64: str # the annotated image, encoded as a string