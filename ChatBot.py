# Simple Rule-Based Chatbot

# Function for chatbot replies
def chatbot(user_input):

    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I am a simple chatbot."

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


print("=== CHATBOT ===")
print("Type 'bye' to exit.\n")

# Chat loop
while True:

    user = input("You: ")

    response = chatbot(user)

    print("Bot:", response)

    # Exit condition
    if user.lower() == "bye":
        break