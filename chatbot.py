from ai_client import ask_ai
import logging
import json
import os

logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

class ChatBot:
    def __init__(self):
        self.history_file = "chat_history.json"
        self.messages = self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                return json.load(file)
        return []
    
    def save_history(self):
        with open(self.history_file, "w") as file:
            json.dump(self.messages, file, indent=4)

    def run(self):
        logging.info("Chatbot started")

        while True:
            user = input("You: ")

            if user.lower() == "bye":
                logging.info("User ended the conversation")
                print("Bot: Goodbye!")
                break

            logging.info(f"User: {user}")

            self.messages.append({
                "role": "user",
                "content": user
            })

            try:
                answer = ask_ai(self.messages)
                logging.info("AI responded successfully")
            except Exception as e:
                logging.error(f"API request failed: {e}")
                answer = f"An error occured: {e}"

            print("Bot:", answer)

            self.messages.append({
                "role": "assistant",
                "content": answer
            })

            self.save_history()