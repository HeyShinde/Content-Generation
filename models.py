from google import genai
from mistralai import Mistral
from config import GEMINI_API_KEY, MISTRAL_API_KEY

# Initialize Gemini API client
genai_client = genai.Client(api_key=GEMINI_API_KEY)

# Initialize Mistral API client
mistral_client = Mistral(api_key=MISTRAL_API_KEY)

def generate_text_gemini(prompt: str) -> str:
    """Generates text using Gemini."""
    response = genai_client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text

def generate_text_mistral(prompt: str) -> str:
    """Generates text using Mistral."""
    chat_response = mistral_client.chat.complete(
        model="mistral-large-latest",
        messages=[{"role": "user", "content": prompt}],
    )
    return chat_response.choices[0].message.content
