import base64
from io import BytesIO
from diffusers import DiffusionPipeline

# Load the Stable Diffusion model
pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
pipe.load_lora_weights("shindeaditya/sdxl-fashion")

def generate_image(prompt: str):
    """Generates an image based on a given prompt."""
    image = pipe(prompt).images[0]  # Generate image

    # Convert image to Base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return img_str
