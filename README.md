# **Terminal Chatbot with OpenAI API**

A Python chatbot that lets you interact with **OpenAI's Chat Completion API** via the terminal. The bot uses your **name** and tracks **token usage** during the conversation.

## **Features**

- **Customizable bot name**: Set the name you want the bot to address you with.
- **Continuous conversation**: Maintain an ongoing chat history.
- **Token usage tracking**: Get the total tokens used when you exit.
- **Secure API key handling**: The API key is loaded from a `.env` file to keep it safe.

## **Requirements**

- **Python 3.x**
- `openai` and `python-dotenv` libraries

## **Setup**

1. **Install dependencies**:

    ```bash
    pip install openai python-dotenv
    ```

2. **Create a `.env` file** with your **OpenAI API key**:

    ```plaintext
    OPENAI_API_KEY=your-api-key-here
    ```

3. **Run the chatbot**:

    ```bash
    python chatbot.py <UserName>
    ```

4. To quit, press **CTRL + D** (or **CMD + D** on macOS).
