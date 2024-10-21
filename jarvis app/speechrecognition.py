import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # Fixed 'vo[ces"'
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # Fixed 'rumAndwait()'

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour>=18 and hour <20:
        speak("Good Evening!")
    elif hour>=20 and hour <24:
        speak("Good Night!")

    speak("I am Jarvis, Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Fixed 'yith' to 'with'
        print("Listening ... ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ... ")
        query = r.recognize_google(audio, language='en-in')  # Fixed 'language' string
        print(f"User said: {query}\n")  # Fixed 'query}' to 'query}'
    except Exception as e:
        # print(e)
        print("Say that again please ... ")
        return "None"  # Fixed 'returm' to 'return'
    return query  # Fixed indentation

if __name__ == "__main__":  # Fixed 'name =w "_main "'
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # Fixed 'im' to 'in'
            speak('Searching Wikipedia ... ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:  # Fixed 'im' to 'in'
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:  # Fixed 'im' to 'in'
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "D:\\songs\\Favorite"  # Fixed quotation mark
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:  # Fixed quotation mark
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Fixed format string
            speak(f"Sir, the time is {strTime}")

        elif "exit" in query or "stop" in query:  # Check for exit commands
            speak("Goodbye! Have a nice day!")  # Optional farewell message
            break  # Exit the loop
