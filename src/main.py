from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):
    uri: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/process-image")
async def process_image(image: Image):
    return image
