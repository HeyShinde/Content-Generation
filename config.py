import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Hugging Face Model
HUGGINGFACE_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"
LORA_WEIGHTS = "shindeaditya/sdxl-fashion"