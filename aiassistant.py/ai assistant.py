import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

#initialise textto speech engine
engine=pyttsx3.init()
engine.setProperty(name='rate', value=150)  # adjust speech speed


#adjust speech speed
def speak(text):
    """speak the given text"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input"""
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

    try:
        command=recognizer.recognize_google(audio).lower()
        print(f"You said:{command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry,I didn't catch that")
        return ""

def execute_command(command):
    """process voice command"""
    if "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")

    elif "search for" in command:
        query=command.replace("search for","").strip()
        speak(f"Searching for {query}")
        pywhatkit.search(query)

    elif "play" in command:
        song=command.replace("play","").strip()
        speak(f"Playing {song} on Youtube")
        pywhatkit.playonyt(song)

    elif "wikipedia" in command:
        topic=command.replace("wikipedia","").strip()
        summary = wikipedia.summary(topic, sentences=1)
        speak(summary)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I didn't understand that command.")

#main loop
speak("Hello Ashwika! How can I assist you?")
while True:
    command=listen()
    if command:
        execute_command(command)