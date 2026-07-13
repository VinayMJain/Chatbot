class ChatBot:
    def __init__(self, name):
        self.name = name

        self.responses = {
            "how are you": "I'm doing great! Thanks for asking.",
            "what is your name": f"My name is {self.name}.",
            "who created you": "Mr. Vinay Jain created me.",
            "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
            "what can you do": "I can answer some specific questions.",
            "what is python": "Python is a high-level, easy-to-learn programming language used for Web development, AI.",
            "what is 10 + 20": "The answer is 30",
            "thank you": "You're welcome!"
        }
        
    def greet(self):
        return f"Hello! I'm {self.name}."

    def goodbye(self):
        return "Goodbye! Have a nice day."

    def get_response(self, message):

        if message in ["hello", "hi", "hey"]:
            return self.greet()
        
        if message == "bye":
            return self.goodbye()

        return self.responses.get(message, "Sorry, I don't understand.")


print("=" * 40)
print("🤖 PyBot")
print("I can answer simple questions.")
print("Type 'bye' to exit.")
print("=" * 40)

bot = ChatBot("PyBot")
while True:
    message = input("You: ").lower()
    response = bot.get_response(message)
    print(f"Bot: {response}")
    if message == "bye":
        break