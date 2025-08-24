from openai import OpenAI
import os
from dotenv import load_dotenv

print("Enter quit or finish to stop chatting.")
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

while True: 
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'finish']:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [
                {"role": "system", "content": "You are an user-friendly chatbot"},
                {"role": "user", "content": "Goodbye!"}
            ]
        )
        print("ChatGPT:", response.choices[0].message.content, "\n")
        break
    else: 
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [
                {"role": "system", "content": "You are an user-friendly chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        print("ChatGPT:", response.choices[0].message.content, "\n")