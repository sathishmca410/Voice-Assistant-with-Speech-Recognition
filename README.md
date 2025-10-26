Voice Assistant with Speech Recognition

Overview

This project is a Python-based Voice Assistant that listens to user commands through voice, processes them, and performs specific tasks such as opening websites, fetching Wikipedia summaries, telling the date/time, and launching system applications like Notepad.
It uses speech recognition for input and text-to-speech synthesis for output, enabling a fully interactive experience.

The assistant can be activated by the wake word “Hey Assistant”, after which it listens for commands and executes them accordingly.

Objective

The main goal of this project is to:

Implement speech recognition and voice response using Python.

Allow the assistant to perform real-time tasks such as searching, opening applications, and giving information.

Demonstrate practical integration of Python libraries like speech_recognition, pyttsx3, wikipedia, datetime, and os.

Provide a smooth and human-like interaction experience using wake-word activation.

Features


✅ Wake-word detection (“Hey Assistant”)

✅ Voice-based commands

✅ Opens websites like YouTube or Google

✅ Fetches information from Wikipedia

✅ Tells date and time

✅ Opens local applications (like Notepad)

✅ Graceful exit (“exit” or “quit”)

✅ Handles unclear or missing voice input

Technology Stack

Component	Description

Language	Python

Voice Input	speech_recognition

Voice Output	pyttsx3

Information Source	wikipedia, requests

System Operations	os, datetime, webbrowser

Working Principle

The assistant waits for the wake word (“Hey Assistant”).

Once triggered, it listens for a voice command.

The input is processed using Google’s Speech Recognition API.

Based on the recognized command, it:

Opens websites (YouTube, Google)

Searches Wikipedia

Tells time/date

Opens local apps like Notepad

If “exit” or “quit” is spoken, the program terminates gracefully.

System Requirements

Software:

Python 3.8 or above

Visual Studio Build Tools (for PyAudio support if needed)

Libraries:

pip install speechrecognition
pip install pyttsx3
pip install wikipedia
pip install requests


Hardware:

Working microphone and speakers/headphones

Project Structure
Voice Assistant with Speech Recognition
│

├── main.py                # Main program file

├── requirements.txt       # Required Python libraries

└── task_result.mp4        # final output

How to Run

Open your terminal or VS Code.

(Optional) Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate


Install the dependencies:

pip install -r requirements.txt


Run the program:

python main.py


Speak “Hey Assistant” to activate, then say commands like:

“What is the time?”

“Open YouTube”

“Search World War 2 on Wikipedia”

“Exit”

Future Enhancements

Add weather and news API integration

Add GUI interface using Tkinter or Streamlit

Add email sending and music playback features

Add voice-controlled system settings (volume, brightness)

Conclusion

This project successfully demonstrates how Python can be used to create a real-time interactive voice assistant capable of performing daily automation tasks. It integrates multiple Python modules to provide a seamless user experience through speech recognition and text-to-speech interaction.
