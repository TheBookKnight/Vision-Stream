from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):
    uri: str
    width: int
    height: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

def process_image_logic(image_uri: str):
    # Placeholder for image processing logic
    print(f"Processed image at {image_uri}")
    return f"{image_uri}/processed"

@app.post("/process-image")
async def process_image(image: Image) -> Image:
    image.uri = process_image_logic(image.uri)
    # Example of cropping logic
    cropped_image = {
        "uri": image.uri,
        "width": image.width / 2,  
        "height": image.height / 2 
    }
    return cropped_image

