import openai

class ChatGPT:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        openai.api_key = self.api_key
        self.model = model
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def query(self):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            return str(e)

# Usage Example
api_key = "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"
chatgpt = ChatGPT(api_key)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    chatgpt.add_message("user", user_input)
    response = chatgpt.query()
    print("ChatGPT:", response)
