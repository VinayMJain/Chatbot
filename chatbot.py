from ai_client import ask_ai

class ChatBot:
    def __init__(self):
        self.messages = []

    def run(self):
        while True:
            user = input("You: ")

            if user.lower() == "bye":
                print("Bot: Goodbye!")
                break

            self.messages.append({
                "role": "user",
                "content": user
            })

            answer = ask_ai(self.messages)
            print("Bot: ", answer)

            self.messages.append({
                "role": "assistant",
                "content": answer
            })