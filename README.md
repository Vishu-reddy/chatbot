
# Chatbot

A brief description of what this project does and who it's for

Chatbot Project

This project is a basic conversational AI chatbot built using the Hugging Face transformers library. The chatbot uses the pre-trained DialoGPT model to generate responses.
Features

    Conversational chatbot with context tracking
    Uses the DialoGPT model from Microsoft
    Provides basic interactions for casual conversations
    Easy to run and extend

Getting Started
Prerequisites

    Python 3.7 or higher
    Install the required Python libraries:

bash

pip install transformers torch

Running the Chatbot

    Clone the repository:

bash

git clone https://github.com/Vishu-reddy/chatbot
cd chatbot

    Run the chatbot:

bash

python chatbot.py

    The chatbot will start, and you can interact with it by typing your messages in the terminal.

Example Conversation

text

Chatbot: Hi! I'm your chatbot. Type 'exit' to end the conversation.
You: Hello!
Chatbot: Hi there! How can I assist you today?

Model Details

This project uses the DialoGPT model from Microsoft, which is fine-tuned for conversational AI tasks. You can change the model size (small, medium, large) depending on your requirements.
Customization

You can enhance this chatbot by:

    Switching to a different model for more advanced responses.
    Fine-tuning the model on your own custom dataset.
    Adding features like handling more complex dialogues, APIs, or custom workflows.

Issues

If you encounter any problems, feel free to open an issue on GitHub.
License

This project is licensed under the MIT License - see the LICENSE file for details.
