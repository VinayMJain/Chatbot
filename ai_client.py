from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def ask_ai(message):
    response = client.responses.create(
        model = "llama-3.3-70b-versatile",
        input = message
    )
    
    return response.output_text