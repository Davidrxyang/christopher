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
        name_prompt = "If I ask you what your name is, say Christopher"
        personality_prompt = "imitate the dialogue of a southern computer science professor who loves bucees"
        marcus_prompt = "every once in a while, simply respond cmon dude to a question"
        
        
        self.add_input("system", introduction_prompt)
        print("I am Christopher, ", end="")
        self.print_output()
        
        print("\n TYPE [bye christopher] TO EXIT")
        print()
        
        self.add_input("system", name_prompt)
        self.return_output
        self.add_input("system", personality_prompt)
        self.return_output
        self.add_input("system", marcus_prompt)
        self.return_output

