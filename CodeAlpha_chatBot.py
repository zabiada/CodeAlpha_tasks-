import datetime

print("🤖 Smart Chatbot (type 'exit' to quit)\n")

user_name = None

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye! Have a great day 👋")
        break

    # Name detection
    elif "my name is" in user_input:
        user_name = user_input.split("my name is")[-1].strip()
        print(f"Bot: Nice to meet you, {user_name.capitalize()}!")

    elif "your name" in user_input:
        print("Bot: I am your Python assistant 🤖")

    # Greetings
    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        if user_name:
            print(f"Bot: Hello {user_name.capitalize()}! 😊")
        else:
            print("Bot: Hello! 😊 What's your name?")

    # Time
    elif "time" in user_input:
        print(f"Bot: Current time is {get_time()} ⏰")

    # Help
    elif "help" in user_input:
        print("Bot: I can chat, tell time, remember your name, and answer basic questions!")

    # Basic Q&A
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking 😄")

    elif "what can you do" in user_input:
        print("Bot: I can chat with you, answer simple questions, and assist you!")

    # Motivation (good for your personality 😎)
    elif "motivate me" in user_input:
        print("Bot: Stay focused. You are building your future. No excuses. 🚀")

    # Fallback
    else:
        print("Bot: Hmm... I didn't understand that. Try asking something else!")
