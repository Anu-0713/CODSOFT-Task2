#Simple chatbot that answers pre entered inputs
def simple_chatbot(user_input):
    # Convert user input to lowercase for easier comparison
    user_input = user_input.lower()

    # Define predefined rules and responses
    greetings = ["hello", "hi", "hey", "howdy"]
    greetings_responses = ["Hello!", "Hi there!", "Hey!", "Howdy!"]

    about_bot = ["who are you", "what are you", "what can you do", "tell me about yourself"]
    about_bot_responses = ["I am a simple chatbot built to respond to predefined queries.", "I'm just a chatbot here to help you!", "I am a basic chatbot designed to chat with you."]

    how_are_you = ["how are you", "how's it going", "how are you doing", "how are you doing today"]
    how_are_you_responses = ["I'm good, thank you for asking!", "I'm doing well, thanks!", "I'm doing fine, how about you?"]

    weather = ["how is the weather today", "what's the weather like today", "how's the weather today"]
    weather_responses = ["It is such a pleasant day today.", "The weather is nice and sunny today.", "It's a beautiful day outside."]

    if user_input == "im well":
        return "Good to know! How may I help you today?"

    # Check user input against predefined rules and provide responses
    if user_input in greetings:
        return greetings_responses[greetings.index(user_input)]
    elif user_input in about_bot:
        return about_bot_responses[0]  # Just return the first response for simplicity
    elif user_input in how_are_you:
        return how_are_you_responses[0]  # Just return the first response for simplicity
    elif user_input in weather:
        return weather_responses[0]  # Just return the first response for simplicity
    elif user_input == "how are you doing today":
        return "I'm well, what about you?"
    else:
        return "Sorry, I don't understand that."

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
