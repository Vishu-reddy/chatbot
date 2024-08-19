from transformers import pipeline, Conversation, AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
model_name = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side='left')
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize the conversational pipeline with appropriate padding
chatbot = pipeline("conversational", model=model, tokenizer=tokenizer, framework="pt", pad_token_id=tokenizer.eos_token_id)

def chat_with_bot():
    print("Chatbot: Hi! I'm your chatbot. Type 'exit' to end the conversation.")
    
    # Create a Conversation object to maintain context
    conversation = Conversation()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Add user input to the conversation
        conversation.add_user_input(user_input)
        
        # Generate response
        response = chatbot(conversation)
        
        # Get the chatbot's latest response
        print(f"Chatbot: {response.generated_responses[-1]}")

if __name__ == "__main__":
    chat_with_bot()
