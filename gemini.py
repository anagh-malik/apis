import google.generativeai as genai
import os
from dotenv import load_dotenv

print("Enter quit or finish to stop chatting.")
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    system_instruction='You are a user friendly chatbot.'
)
chat = model.start_chat()
while True:
    user_input = input("User: ")
    if user_input.lower() in ['quit', 'finish']:
        response = chat.send_message("Goodbye!")
        print("Gemini:", response.text, "\n")
        break
    else:
        response = chat.send_message(user_input)
        print("Gemini:", response.text, "\n")