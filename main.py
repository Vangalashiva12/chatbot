from dotenv import load_dotenv
import os

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

print("Hello, iam dupki")

while True:
    user_input = input("You:")
    if user_input == "exit":
        break
    print(f"thanks for sharing {user_input}")
