import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Sir!")
    else:
        speak("Good Evening, Sir!")
    speak("Hi! I'm your personal Jarvis")


def speak(audio, voiceRate=200):
    engine.setProperty('rate', voiceRate)
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query


def joke():
    temp_joke = pyjokes.get_joke()
    print(temp_joke)
    speak(temp_joke, 150)


def wikipedia_search(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia,")
    speak(results)


def open_youtube():
    webbrowser.open("youtube.com")


def send_mail():
    pass


def google_search():
    speak("What do you want to search, Sir?")
    search = takeCommand().lower()
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(search)


def shut_down():
    os.system("shutdown /s /t 1")


def restart():
    os.system("shutdown /r /t 1")


if __name__ == "__main__":
    wishMe()
    running = True
    while running:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            wikipedia_search(query)

        elif 'youtube' in query:
            open_youtube()

        elif 'gmail' in query:
            send_mail()

        elif 'google' in query:
            google_search()

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is " + time)

        elif 'shut down' in query:
            shut_down()

        elif 'restart' in query:
            restart()

        elif 'joke' in query:
            joke()

        elif 'end' in query or 'stop' in query or 'offline' in query:
            speak("Going offline, Goodbye Sir.")
            running = False
