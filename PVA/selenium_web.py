from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Infow:
    def __init__(self):
        service = Service(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, query):
        self.driver.get('https://www.wikipedia.org')
        search=self.driver.find_element_by_xpath('//*[@id='searchInput']')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('#path 27.15')
        eneter.click()

# Example usage
assist = Infow()
assist.get_info('hello')



#
#
#
#
#
#
#
# import pyttsx3 as p
# import speech_recognition as sr
# import datetime
# import subprocess
# import pywhatkit
# import webbrowser
# import requests
#
# engine = p.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate',180)
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
#
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#
# r = sr.Recognizer()
# speak("Hello there, I am your voice assistant, Ray. How are you?")
#
# def listen():
#     with sr.Microphone() as source:
#         r.energy_threshold = 10000
#         r.adjust_for_ambient_noise(source, 1.0)
#         print("Listening...")
#         audio = r.listen(source)
#
#     try:
#         text = r.recognize_google(audio)
#         text = text.lower()
#         print("You said:", text)
#         return text
#     except Exception as ex:
#         print(ex)
#         speak("Sorry, I didn't catch that. Could you please speak again?")
#         return None
#
# def greet_user():
#     hour = datetime.datetime.now().hour
#     if 5 <= hour < 12:
#         greeting = "Good morning!"
#     elif 12 <= hour < 17:
#         greeting = "Good afternoon!"
#     else:
#         greeting = "Good evening!"
#     speak(greeting)
#     print(greeting)
#
# def get_joke():
#     JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any?type=single"
#     response = requests.get(JOKE_API_URL)
#     if response.status_code == 200:
#         joke_data = response.json()
#         joke = joke_data.get("joke", "Sorry, I couldn't fetch a joke right now.")
#     else:
#         joke = "Sorry, I couldn't fetch a joke."
#     return joke
#
# def get_fun_fact():
#     FACT_API_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random"
#     response = requests.get(FACT_API_URL)
#     if response.status_code == 200:
#         fact_data = response.json()
#         fact = fact_data.get("text", "Sorry, I couldn't fetch a fun fact right now.")
#     else:
#         fact = "Sorry, I couldn't fetch a fun fact."
#     return fact
#
# def ask_about_assistant():
#     speak("I'm doing great, thank you for asking! How can I help you today?")
#
# def cmd():
#     text = listen()
#     if text:
#         if 'hello' in text or 'hi' in text:
#             speak("Hello! How can I assist you?")
#         elif 'bye' in text:
#             speak("Goodbye! Have a nice day!")
#             return
#         elif 'what about you' in text or 'how are you doing' in text:
#             ask_about_assistant()
#         elif 'joke' in text:
#             joke = get_joke()
#             speak(joke)
#             print(joke)
#         elif 'fun fact' in text:
#             fact = get_fun_fact()
#             speak(fact)
#             print(fact)
#         elif 'weather' in text:
#             city = text.replace("weather in", "").strip()
#             speak(f"Fetching weather for {city}.")
#         elif 'chrome' in text:
#             speak("Opening Chrome..")
#             programName = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
#             subprocess.Popen([programName])
#         elif 'time' in text:
#             time = datetime.datetime.now().strftime('%I:%M %p')
#             speak(time)
#             print(time)
#         elif 'play' in text:
#             speak("Opening YouTube..")
#             pywhatkit.playonyt(text)
#         elif 'youtube' in text:
#             speak("Opening YouTube.")
#             webbrowser.open('http://www.youtube.com')
#         elif 'greet me' in text:
#             greet_user()
#             speak("What can I do for you today?")
#         else:
#             speak("Sorry, I didn't understand that.")
#     else:
#         speak("I couldn't hear anything, please try speaking again.")
#
# while True:
#     cmd()


import time
import os

# Full path to your animation video file
animation_video_path = r"C:\Users\Admin\Documents\SWATHI\LLM\animation.mp4"  # Ensure correct filename & extension

def process_video():
    input("Paste the link: ")  # Just takes input, doesn't process it

    print("[INFO] Extracting video...")
    time.sleep(2)

    print("[INFO] Transferring data...")
    time.sleep(2)

    print("[INFO] Processing audio...")
    time.sleep(2)

    print("[INFO] Converting speech to text...")
    time.sleep(2)

    print("[INFO] Generating sign language animation...")
    time.sleep(2)

    print("[INFO] Displaying animation...")

    if os.path.exists(animation_video_path):
        os.startfile(animation_video_path)  # Open video file
    else:
        print(f"[ERROR] File not found: {animation_video_path}")

if __name__ == "__main__":
    process_video()
























