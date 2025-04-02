from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import generate_text_gemini, generate_text_mistral
from image_generator import generate_image
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class TextRequest(BaseModel):
    model: str
    prompt: str

class ImageRequest(BaseModel):
    prompt: str

@app.post("/generate_text/")
async def generate_text(request: TextRequest):
    """Generate text using Gemini or Mistral."""
    if request.model.lower() == "gemini":
        text = generate_text_gemini(request.prompt)
    elif request.model.lower() == "mistral":
        text = generate_text_mistral(request.prompt)
    else:
        raise HTTPException(status_code=400, detail="Invalid model name")
    
    return {"text": text}

@app.post("/generate_image/")
async def generate_image_endpoint(request: ImageRequest):
    """Generate an image and return Base64 encoded data."""
    try:
        img_str = generate_image(request.prompt)
        return JSONResponse(content={"image": f"data:image/png;base64,{img_str}"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
