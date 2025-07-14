import google.generativeai as genai

API_key = "AIzaSyDZ8rASdvMKWdcMRU19MW1gKaLBmnWg840"
genai.configure(api_key=API_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

chat = model.start_chat()

print("Welcome to the AI chat! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Ending the chat. Goodbye!")
        break
    response = chat.send_message(user_input)
    print(f"AI: {response.text}")
