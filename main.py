import json
import random

class ChatBot:

    def __init__(self, intent: str) -> None:

        with open(intent) as json_file:

            self.intents = json.load(json_file)

# -------------------------------------------------------------------------- #

    def userInput(self, message: str):

        for intent in self.intents['intents']:

            if message in intent['patterns'] and intent['tag'] == 'goodbye':

                return "nan"

            if message in intent['patterns']:

                responses = intent['responses']

                return random.choice(responses)
            
        return "I'm sorry, Can you please provide more information?" 
    
# -------------------------------------------------------------------------- #


    def chatbot_function(self):

        print("ChatBot: Hello! How can I assist you?")

        while True:

            user_input = input("User: ").strip()

            response = self.userInput(user_input)

            if response == "nan":

                print("ChatBot: ", "Good bye!")

                break

            print("ChatBot: ", response)

# -------------------------------------------------------------------------- #

chat = ChatBot('intent.json')
chat.chatbot_function()