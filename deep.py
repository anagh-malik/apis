import requests
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")
url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}"
}
print("Enter quit or finish to stop chatting.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'finish']:
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are an user friendly chat assistant."},
                {"role": "user", "content": "Goodbye"}
            ]
        }
        response = requests.post(url, headers=headers, json=data)
        print(response.json())
    else: 
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "Your are an user friendly chat assistant."},
                {"role": "user", "content": user_input}
            ]
        }
        response = requests.post(url, headers=headers, json=data)
        print(response.json())
