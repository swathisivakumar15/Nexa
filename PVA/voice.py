# import pyttsx3 as p
# import speech_recognition as sr
#
#
# engine = p.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate',180)
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
#
# def speak(text):
#
#     engine.say(text)
#     engine.runAndWait()
#
#
# r=sr.Recognizer()
#
# speak('Hello there I am your voice assistant ,Ray.  How are you')
#
# with sr.Microphone() as source:
#     r.energy_threshold=10000
#     r.adjust_for_ambient_noise(source,1.2)
#     print('listening')
#     audio=r.listen(source)
#     text=r.recognize_google(audio)
#     print(text)
# if 'what' and 'about' and 'you' in text:
#     speak("I am having good day")
# speak("What can I do for you")
import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print('Please speak...')
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
        speak("Sorry, I'm having trouble with the speech recognition service. Please try again later.")
        return None

speak("Hello there, I am your voice assistant. How can I help you today?")
while True:
    text = listen()
    if text:
        if 'hello' in text:
            speak("Hello! How can I assist you?")
        elif 'how are you' in text:
            speak("I'm doing great, thank you!")
        elif 'bye' in text:
            speak("Goodbye! Have a nice day!")
            break
        else:
            speak("I didn't understand that. Can you please try again?")
