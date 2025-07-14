import google.generativeai as genai
import speech_recognition as sr
import pyttsx3


API_key = "AIzaSyDZ8rASdvMKWdcMRU19MW1gKaLBmnWg840"
genai.configure(api_key=API_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
chat = model.start_chat()


engine = pyttsx3.init()
engine.setProperty('rate', 160)  
recognizer = sr.Recognizer()
mic = sr.Microphone()

def speak(text):
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

print("Voice Assistant is running. Say 'exit' to quit.")

while True:
    with mic as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        user_input = recognizer.recognize_google(audio)
        print(f"You: {user_input}")

        if user_input.lower() == "exit":
            speak("Ending the conversation. Goodbye!")
            break

        response = chat.send_message(user_input)
        speak(response.text)
        
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
