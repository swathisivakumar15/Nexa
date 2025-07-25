import pyttsx3 as p
import speech_recognition as sr
import datetime
import pywhatkit
import webbrowser
import wikipedia

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f'You said: {text}')
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please speak again?")
        return None
    except sr.RequestError:
        speak("Sorry, I'm having trouble with the speech recognition service. Please try again.")
        return None

def fetch_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        print(f"According to database, {summary}")
        speak(f"According to database, {summary}")

    except wikipedia.exceptions.DisambiguationError as e:
        speak("The topic is too ambiguous. Please specify your question further.")
        print(e)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information on that topic.")
    except Exception as e:
        speak("Something went wrong while fetching information.")
        print(e)

speak("Hello there, I am your NDE voice assistant. How can I help you today?")
while True:
    text = listen()
    if text:
        if 'hello' in text:
            speak("Hello! How can I assist you?")
        elif 'your name' in text:
            speak("I'm Nexa")
        elif 'how are you' in text or 'what about you' in text:
            speak("I'm doing great, thank you!")
        elif 'bye' in text:
            speak("Goodbye! Have a nice day!")
            break
        elif 'play' in text:
            speak("Opening YouTube to play your request.")
            pywhatkit.playonyt(text)
        elif 'time' in text:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {current_time}.")
            print(current_time)
        elif 'youtube' in text:
            speak("Opening YouTube.")
            webbrowser.open('http://www.youtube.com')
        elif 'weather' in text:
            city = text.replace("weather in", "").strip()
            speak(f"Fetching weather for {city}.")
            # Add weather report code if needed
        elif 'search' in text or 'who is' in text or 'what is' in text:
            query = text.replace("search", "").replace("who is", "").replace("what is", "").strip()
            fetch_wikipedia(query)

        else:
            speak("I didn't understand that. Can you please try again?")
