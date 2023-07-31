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

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


entry = None
stop_flag = False  # Define the stop_flag variable at the top of the script


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


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        speak("say something")
        recognizer.pause_threshold = 0.8
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for 1 second of ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        speak("recognizing")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


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
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location.replace(" ", "+"))


        elif 'exit' in query:
            speak("thanks for giving your time")
            stop_voice_assistant()


def stop_voice_assistant():
    global stop_flag
    speak("Stopping the Voice Assistant.")
    stop_flag = True


def start_voice_assistant():
    global stop_flag
    wish_time()
    perform_task()
    stop_flag = False  # Reset the flag to False when starting the voice assistant


def main():
    # Create the main GUI window
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("500x700")
    root.configure(bg=BG_COLOR)

    def on_button_click():
        global stop_flag
        if not stop_flag:
            stop_flag = False  # Reset the flag to False when starting the voice assistant
            Thread(target=start_voice_assistant).start()
        else:
            stop_voice_assistant()

    # Load and set the background image
    background_image = Image.open(
        "wallpaperflare.com_wallpaper.jpg")  # Replace "path/to/your/background_image.jpg" with the actual image file path
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = ttk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    f1 = ttk.Frame(root)
    f1.pack(pady=100)  # Add some padding to the frame to center it vertically

    image2 = Image.open("p.jpg")  # Replace "path_to_image2.jpg" with the actual path to your image
    resized_image = image2.resize((120, 120))
    p2 = ImageTk.PhotoImage(resized_image)
    l2 = ttk.Label(f1, image=p2, relief=SUNKEN)
    l2.pack(side="top", fill="both")

    # Heading
    heading_label = ttk.Label(root, text="Voice Assistant", font=HEADING_FONT, background=BG_COLOR)
    heading_label.pack(pady=20)

    global entry
    f1 = ttk.Frame(root)
    f1.pack()
    l1 = ttk.Label(f1, text="Enter Your Name", font=INSTRUCTION_FONT, background=BG_COLOR)
    l1.pack(side=LEFT, fill=BOTH)
    entry = ttk.Entry(f1, width=30)
    entry.pack(pady=10)

    # Instruction
    instruction_label = ttk.Label(root, text="Click the button below to start the Voice Assistant.",
                                  font=INSTRUCTION_FONT, background=BG_COLOR)
    instruction_label.pack(pady=10)

    # Create and place a button on the GUI
    button = ttk.Button(root, text="Start Voice Assistant", command=on_button_click,
                        style="VoiceAssistant.TButton")
    button.pack(pady=20)

    # Style the button
    style = ttk.Style(root)
    style.configure("VoiceAssistant.TButton", font=BUTTON_FONT, background=BUTTON_COLOR, foreground=BUTTON_FOREGROUND)

    # Run the GUI main loop
    root.mainloop()


if __name__ == "__main__":
    main()