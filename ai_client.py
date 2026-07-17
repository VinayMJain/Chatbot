from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def ask_ai(messages):
    response = client.responses.create(
        model = "llama-3.3-70b-versatile",
        input = messages
    )
    
    return response.output_text