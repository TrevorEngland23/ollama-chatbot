import ollama

def ollama_chatbot(prompt):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = ollama_chatbot(user_input)
        print("\nChatbot:", response, "\n")