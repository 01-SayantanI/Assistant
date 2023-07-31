# Assistant
**This Python Voice Assistant with GUI is a user-friendly application designed to interact with users using voice commands and provides a graphical user interface (GUI) for easy control. The assistant is capable of performing various tasks based on user input.**

![Screenshot (54)](https://github.com/01-SayantanI/Assistant/assets/140982719/b52e2047-f938-4a98-b6e9-911766b8805b)


This Python Voice Assistant with GUI uses Tkinter to enable users to interact through voice commands. It performs tasks like Wikipedia searches,google searches, YouTube music playback, website opening, providing a fun and interactive voice-based experience.



**Features:**
-------------------
***Speech Recognition: Utilizes the speech_recognition module to recognize user's speech through the microphone, enabling seamless communication with the assistant.***

***Text-to-Speech: Implements pyttsx3 to convert the assistant's responses into speech, allowing it to interact audibly with the user.***

***Wikipedia Search: Enables users to query information from Wikipedia by using the wikipedia module to access relevant summaries.***

***YouTube Music Player: Allows users to play their favorite songs on YouTube by utilizing the pywhatkit module to search and play music videos.***

***Web Browsing: Provides convenient access to YouTube and Google using the webbrowser module, allowing users to open these sites quickly.***

***Joke Generator: Amuses users with jokes retrieved from the pyjokes module.***

***Current Time Display: Informs users of the current time through voice feedback using the datetime module.***

***Location Search: Assists users in locating places through Google Maps with the help of the webbrowser module.***

***User Interaction: The assistant prompts users to enter their names and greets them accordingly, creating a personalized experience.***

**Instructions for GUI:**
-------------------------------
***Click the "Start Voice Assistant" button to initiate the assistant's operation.***

***Once started, users can communicate with the assistant using voice commands.***

***Saying "exit" stops the assistant and displays a gratitude message.***

***Users can restart the assistant by clicking the button again.***

Modules Used:
------------------
pyttsx3: For converting text to speech.

datetime: For handling date and time-related functions.

speech_recognition (sr): For recognizing speech from the microphone.

wikipedia: To access information from Wikipedia.

os: For starting applications on the system.

webbrowser: For opening websites in the default web browser.

pyjokes: To generate random jokes for entertainment.

pywhatkit (kit): For playing songs on YouTube and performing web searches.

time: For handling time-related operations.

plyer.notification: For showing notifications.


Modules to Install:
-----------------------------
pyttsx3: pip install pyttsx3

speech_recognition: pip install SpeechRecognition

wikipedia: pip install wikipedia-api

pywhatkit: pip install pywhatkit

plyer: pip install plyer

tkinter: Pre-installed with Python (no need for separate installation).

PIL (Pillow): pip install pillow (for handling images).


This project offers an engaging and functional voice assistant with a GUI, providing a user-friendly interface for various tasks and enjoyable interactions.

**This project is continuously evolving, and more features will be added over time. You can also contribute to the project by adding your own unique features and enhancements. Future planned features include email sending, reminders, calendar events, and more. If you have any new ideas or want to collaborate on enhancing the Voice Assistant's functionality, feel free to create pull requests or open issues on the repository. Contributions from the open-source community are warmly welcomed!**

**code**
--------------
# Import necessary libraries
import pyttsx3

import datetime

import speech_recognition as sr

import wikipedia

import os

import webbrowser

import pyjokes

import pywhatkit as kit

import time

from plyer import notification

import tkinter as tk

from tkinter import ttk

from tkinter import LEFT, BOTH, SUNKEN

from PIL import Image, ImageTk

from threading import Thread

# Constants for custom styling
BG_COLOR = "#D2C6E2"

BUTTON_COLOR = "#F9F4F2"

BUTTON_FONT = ("Arial", 14, "bold")

BUTTON_FOREGROUND = "black"

HEADING_FONT = ("white", 24, "bold")

INSTRUCTION_FONT = ("Helvetica", 14)

INSTRUCTION_FONT1 = ("Helvetica", 14)

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

# Global variables
entry = None

stop_flag = False  # Define the stop_flag variable at the top of the script

# Function to speak the given text
def speak(audio):

    engine.say(audio)
    
    engine.runAndWait()

# Function to greet the user based on the time of the day
def wish_time():

    global entry
    
    x = entry.get()
    
    hour = int(datetime.datetime.now().hour)
    
    if 0 <= hour < 6:
    
        speak('Good night! Sleep tight.')
        
    elif 6 <= hour < 12:
    
        speak('Good morning!')
        
    elif 12 <= hour < 18:
    
        speak('Good afternoon!')
        
    else:
    
        speak('Good evening!')
        
    speak(f"{x} How can I help you?")

# Function to listen to user's command from the microphone
def take_command():

    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
    
        print("Say something:")

        speak("Say something")
        
        recognizer.pause_threshold = 0.8
        
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for 1 second of ambient noise
        
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        
        speak("Recognizing")
        
        query = recognizer.recognize_google(audio, language='en-in')
        
        print(f"You said: {query}")
        
    except Exception as e:
    
        print("Say that again please...")
        
        return "None"
        
    return query
    

# Function to perform different tasks based on user's query
def perform_task():

    global stop_flag
    
    while not stop_flag:
    
        query = take_command().lower()  # Converting user query into lower case

        
        if 'wikipedia' in query:
        
            speak('Searching Wikipedia...')
            
            query = query.replace("wikipedia", "")
            
            try:
                results = wikipedia.summary(query, sentences=2)
                
                speak("According to Wikipedia")
                
                print(results)
                
                speak(results)
                
            except wikipedia.exceptions.DisambiguationError as e:
            
                # Handle disambiguation error (when the search term has multiple possible meanings)
                
                print(f"There are multiple meanings for '{query}'. Please be more specific.")
                
                speak(f"There are multiple meanings for '{query}'. Please be more specific.")
                
            except wikipedia.exceptions.PageError as e:
            
                # Handle page not found error (when the search term does not match any Wikipedia page)
                
                print(f"'{query}' does not match any Wikipedia page. Please try again.")
                
                speak(f"'{query}' does not match any Wikipedia page. Please try again.")
                
        elif 'play' in query:
        
            song = query.replace('play', "")
            
            speak("Playing " + song)
            
            kit.playonyt(song)
            
        elif 'open youtube' in query:
        
            webbrowser.open("https://www.youtube.com/")
            
        elif 'open google' in query:
        
            webbrowser.open("https://www.google.com/")
            
        elif 'search' in query:
        
            s = query.replace('search', '')
            
            kit.search(s)
            
        elif 'the time' in query:
        
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            
            speak(f"Sir, the time is {str_time}")
            
        elif 'open code' in query:
        
            code_path = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            
            os.startfile(code_path)
            
        elif 'joke' in query:
        
            speak(pyjokes.get_joke())
            
        elif "where is" in query:
        
            query = query.replace("where is", "")
            
            location = query.strip()
            
            speak("User asked to locate")
            
            speak(location)
            
            webbrowser.open("https://www.google.com/maps/place/" + location.replace(" ", "+"))

            
        elif 'exit' in query:
        
            speak("Thanks for giving your time.")
            
            stop_voice_assistant()

# Function to stop the voice assistant
def stop_voice_assistant():

    global stop_flag
    
    speak("Stopping the Voice Assistant.")
    
    stop_flag = True
    

# Function to start the voice assistant
def start_voice_assistant():


    wish_time()
    
    perform_task()
    
    stop_flag = False  # Reset the flag to False when starting the voice assistant

# Function to create the main GUI window and handle button click events

def main():

    # Create the main GUI
