import os
from dotenv import load_dotenv
import sys
from openai import OpenAI

def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide your username. Usage: python3 chatbot.py UserName")
    userName = sys.argv[1]
    
    # Check API Key and verify license
    API_KEY = getLicense()
    if not API_KEY:
        return sys.exit("Error: OPENAI_API_KEY not set in the environment.")
    
    isValid, e = checkLicense(API_KEY)
    if not isValid:
        return sys.exit(f"Error: Invalid OPENAI_API_KEY.\nDetails: {e}")
    
    client = OpenAI()
    
    # Start the conversation
    messages = []
    messages.append({"role": "system", "content": f"You are a helpful assistant, who calls me by name {userName}"})
    print()
    print("Welcome to terminal AI assistant! In order to quit, press CTRL + D.")
    print("Please enter your first message:")
    while True:
        try:
            userMessage = input("> " + userName + ": ").strip()
            botResponse, usedTokens = chatWithAssistant(client, userMessage, messages)
            print("> AI:", botResponse)
            continue
        except KeyboardInterrupt:
            print()
            print("Bye!")
            sys.exit(f"Tokens Used: {usedTokens}")
        except EOFError:
            print()
            print("Bye!")
            sys.exit(f"Tokens Used: {usedTokens}")
    
    
def getLicense():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")

def checkLicense(api_key):
    client = OpenAI(api_key=api_key)
    try:
        # Small API call to check if authentication or other exceptions are raised
        response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ],
            model="o1-mini",
            max_completion_tokens=5,
        )
        return True, None
    except Exception as e:
        #return False, type(e).__name__
        return False, e

def chatWithAssistant(client, userInput, messages):
    messages.append({"role": "user", "content": userInput})
    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = messages,
        )
        
        tokensUsed = response.usage.total_tokens
        # index 0 because OpenAI offers multiple possible answer options
        botResponse = response.choices[0].message.content
        return botResponse, tokensUsed
    
    except client.APIError as e:
        print("Received Error while using OpenAI API: " + type(e).__name__)
        print("Details: ", e)
        sys.exit(1)
        

if __name__ == "__main__":
    main()