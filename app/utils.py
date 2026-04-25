import cv2
import numpy as np
from app.model import get_face_app

def extract_embedding(image_bytes):
    # Convert bytes → numpy image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return None

    app = get_face_app()
    faces = app.get(img)

    if len(faces) == 0:
        return None

    # Take first face only (MVP)
    embedding = faces[0].embedding

    return embedding.tolist()