#creating an ai assitand seripously to help people with their daily tasks and make their lives easier. with no classses or objects
import openai
openai.api_key = 'your-api-key-here'
def ask_ai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
#WE WILL MAKE IT LIKE IT WILL NEVER SAY IT IS CHATGPT OR OPENAI
def main():
    print("Hello! I'm your personal AI assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("AI Assistant: Goodbye! Have a great day!")
            break
        response = ask_ai(user_input)
        print(f"AI Assistant: {response}")
if __name__ == "__main__":
    main()
    