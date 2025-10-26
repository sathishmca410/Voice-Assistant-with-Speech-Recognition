import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import requests
import sys

# --- Initialize recognizer and voice engine ---
r = sr.Recognizer()
engine = pyttsx3.init()

# Set speaking rate and voice
engine.setProperty("rate", 175)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id if len(voices) > 1 else voices[0].id)  # Female if available

def speak(text):
    """Always speak the text and print it safely."""
    try:
        print("Assistant:", text.encode(sys.stdout.encoding, errors='ignore').decode(sys.stdout.encoding))
    except Exception:
        print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture user voice and return recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="en-in")
        print(f"User said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def get_weather(city="Chennai"):
    """Fetch weather info from wttr.in"""
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "I couldn't fetch the weather right now."
    except Exception:
        return "Unable to connect to the weather service."

def main():
    speak("Hey, I am your assistant. Say 'Hey assistant' to start.")
    while True:
        with sr.Microphone() as source:
            print("Waiting for wake-word...")
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in").lower()
            print(f"User said: {query}")
        except sr.UnknownValueError:
            continue
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            continue

        if "hey assistant" in query or "hi assistant" in query:
            speak("Yes, I am listening. What can I do?")
            while True:
                command = listen()
                if not command:
                    speak("Sorry, I didn't catch that. Can you repeat please?")
                    continue

                # Exit
                if "exit" in command or "quit" in command or "stop" in command:
                    speak("Goodbye! Have a great day!")
                    return

                # Time and date
                elif "today time" in command:
                    time_str = datetime.datetime.now().strftime("%I:%M %p")
                    speak(f"The time is {time_str}")

                elif "today date" in command or "today" in command:
                    date_str = datetime.datetime.now().strftime("%A, %B %d, %Y")
                    speak(f"Today is {date_str}")

                # Open websites
                elif "open youtube" in command:
                    speak("Opening YouTube")
                    webbrowser.open("https://www.youtube.com")

                elif "google" in command:
                    speak("Opening Google")
                    webbrowser.open("https://www.google.com")

                elif "search wikipedia" in command:
                    speak("What should I search on Wikipedia?")
                    topic = listen()
                    if topic:
                        try:
                            result = wikipedia.summary(topic, sentences=2)
                            speak(result)
                        except Exception:
                            speak("Sorry, I couldn't find that on Wikipedia.")
                    else:
                        speak("I didn't catch that.")

                elif "weather" in command:
                    speak("Which city's weather do you want?")
                    city = listen()
                    if city:
                        weather_info = get_weather(city)
                        speak(weather_info)
                    else:
                        speak("I didn’t catch the city name.")

                elif "open notepad" in command:
                    speak("Opening Notepad")
                    os.system("notepad")

                else:
                    # This ensures **all fallback responses are spoken**
                    speak("Sorry, I didn’t understand that. Please try again.")

        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
