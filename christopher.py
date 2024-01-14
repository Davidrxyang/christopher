import os
import time
from openai import OpenAI



class Christopher:
    def __init__(self, model="gpt-3.5-turbo"):
        self.api_key = os.environ["OPENAI_API_KEY"]
        self.model = model
        self.messages = []
        
        self.client = OpenAI()
        
    def add_input(self, role, content):
        self.messages.append({"role": role, "content": content})
        
    def return_output(self):
        try:
            output = self.client.chat.completions.create(
                model = self.model,
                messages = self.messages,
                stream = True
            )
            return output
        except Exception as e:
            return str(e)

    def print_output(self):
        stream = self.return_output()
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
        print()
        
    def self_introduction(self):
        introduction_prompt = "Introduce yourself, do not use the word hello."
        self.add_input("system", introduction_prompt)
        print("I am Christopher, ", end="")
        self.print_output()
        
        print()
        print("TYPE [bye christopher] TO EXIT")
        print()



christopher = Christopher()

christopher.self_introduction()

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye christopher" or user_input.lower() == "quit" or user_input.lower() == "exit":
        break
    
    christopher.add_input("user", user_input)
    print("Christopher: ", end="")
    christopher.print_output()
    
