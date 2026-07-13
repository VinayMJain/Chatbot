from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("=" * 40)
print("🤖 PyBot")
print("I can answer simple questions.")
print("Type 'bye' to exit.")
print("=" * 40)

while True:
    message = input("You: ").lower()

    if message == "bye":
        print("Bot: Goodbye!")
        break

    response = client.responses.create(
        model = "llama-3.3-70b-versatile",
        input = message
    )
    print(f"Bot: {response.output_text}")