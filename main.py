import json
import random

class ChatBot:

    def __init__(self, intent: str) -> None:

        with open(intent) as json_file:

            self.intents = json.load(json_file)

# -------------------------------------------------------------------------- #

    def userInput(self, message: str):

        for intent in self.intents['intents']:

            if message in intent['patterns']:

                if intent['tag'] == 'goodbye':

                    return random.choice(intent['responses']), True
                
                else:

                    return random.choice(intent['responses']), False
            
        return "I'm sorry, Can you please provide more information?" 
    
# -------------------------------------------------------------------------- #


    def chatbot_function(self):

        print("ChatBot: Hello! How can I assist you?")

        while True:

            user_input = input("User: ").strip()

            response, end_program = self.userInput(user_input)

            print("ChatBot:", response)

            if end_program:
                
                break

# -------------------------------------------------------------------------- #

chat = ChatBot('intent.json')
chat.chatbot_function()