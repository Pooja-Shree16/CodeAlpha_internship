print("========================================")
print("      🤖 Welcome to CodeAlpha ChatBot")
print("========================================")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("🤖 ChatBot: Hi! How are you?")

    elif user == "hi":
        print("🤖 ChatBot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("🤖 ChatBot: I am fine. Thank you!")

    elif user == "your name":
        print("🤖 ChatBot: My name is CodeAlpha Bot.")

    elif user == "who created you":
        print("🤖 ChatBot: I was created by Pooja Shree G.")

    elif user == "what can you do":
        print("🤖 ChatBot: I can answer simple questions and chat with you.")

    elif user == "good morning":
        print("🤖 ChatBot: Good Morning! Have a wonderful day!")

    elif user == "good afternoon":
        print("🤖 ChatBot: Good Afternoon!")

    elif user == "good evening":
        print("🤖 ChatBot: Good Evening!")

    elif user == "good night":
        print("🤖 ChatBot: Good Night! Sweet dreams!")

    elif user == "thank you":
        print("🤖 ChatBot: You're welcome!")

    elif user == "bye":
        print("🤖 ChatBot: Goodbye! Have a nice day.")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand. Please try another question.")