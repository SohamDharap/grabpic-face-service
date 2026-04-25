from fastapi import FastAPI, UploadFile, File, HTTPException
from app.utils import extract_embedding

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/embed")
async def embed(file: UploadFile = File(...)):
    contents = await file.read()

    embedding = extract_embedding(contents)

    if embedding is None:
        raise HTTPException(status_code=400, detail="No face detected")

    return {
        "embedding": embedding
    } 