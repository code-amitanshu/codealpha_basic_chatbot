def chatbot():
    print("Chatbot: Hello! I am a simple Python chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Chatbot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How are you?")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()