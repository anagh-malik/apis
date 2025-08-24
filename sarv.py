from sarvamai import SarvamAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("SARVAM_API_KEY")
client = SarvamAI(api_subscription_key=api_key)
print("Tools are: \n1. Translate\n2. Text-to-speech\n3. Chat")
tool = input("Choose tool = ")
while tool.lower() not in ["translate", "text-to-speech", "chat"]:
    tool = input("Please choose one of the tools in the list: ")
    break
if tool.lower() == "translate":
    while True:
        user_translate = input("Enter text: ")
        response = client.text.translate(
            input=user_translate,
            source_language_code="auto",
            target_language_code="hi-IN"
        )
        print(response, "\n")
        break
elif tool.lower() == "text-to-speech":
    while True:
        user_speech = input("Enter text: ")
        response = client.text_to_speech.convert(
            text=user_speech,
            target_language_code="hi-IN"
        )
        print(response, "\n")
        break
elif tool.lower() == "chat":
    while True:
        print("Type quit or finish to stop chatting.")
        user_input = input("You: ")
        if user_input.lower() in ["quit" or "finish"]:
            response = client.chat.completions(
                model="sarvam-m:free",
                messages = [
                    {"role": "system", "content": "You are an user-friendly chatbot."},
                    {"role": "user", "content": "Goodbye!"}
                ]
            )
            print(response, "\n")
            break
        else:
            response = client.chat.completions(
                model="sarvam-m:free",
                messages = [
                    {"role": "system", "content": "You are an user-friendly chatbot."},
                    {"role": "user", "content": user_input}
                ]
            )
            print(response, "\n")
