import os
# WebBrowser Module
import webbrowser as wb
# Python Text to Speech Module
import pyttsx3
# Used for Date and time
import datetime
# Python Speech recognition module
import speech_recognition as sr
# Used for speech recognition
import pyaudio
# Python wikipedia module
import wikipedia
# Python jokes Library Module
import pyjokes
# Used to Take a screenshot
import pyautogui
# Used to Read Json files
import json
import requests
from urllib.request import urlopen
import time
engine = pyttsx3.init()

# Speak Function


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to Return Today's Date


def todaysDate():
    Date = datetime.datetime.today().strftime("%D")
    speak("Today is ")
    speak(Date)

# Function to Return Current Time


def currentTime():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("Current time is")
    speak(Time)

# Starting Function , Used for Initial Greetings


def greetings():
    speak("Welcome Back Saahil!, This is your personal AI Assistant RAJ")

# Function to Take speech Command from the User and Recognise it


def takeSpeech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-US')
        print(query)
        speak(query)
    except Exception as e:
        print(e)
        print("Unable to Recognise, Please try Again")
        return "None"
    return query


# Main function
if __name__ == "__main__":
    # Starting the File with Initial Greeting
    greetings()

    while True:
        query = takeSpeech().lower()

        # If User asks for Time
        if 'time' in query:
            currentTime()

        # If User asks for Date
        elif 'date' in query:
            todaysDate()

        # If User asks for Wikipedia query
        elif 'wikipedia' in query:
            speak("Searching Wikipedia for you")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
            # ToDo --- Fix Wiki

        # If User asks to Search query in Chrome
        elif 'search in chrome' in query:
            speak("What should I Search for you?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

            search = takeSpeech().lower()
            wb.open('https://www.google.com/search?q='+search)

        # If User asks to Redirect to a Website
        elif 'website' in query:
            speak("Which website do you want me to open?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

            goto = takeSpeech().lower()
            while goto != 'none':
                # wb.get(chromepath).open_new_tab(goto+'.com')
                wb.open('http://www.' + goto + '.com')
                goto = 'none'

        # If User wants to Search Something on YouTube
        elif 'search youtube' in query:
            speak("What do you want to search on Youtube?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            yt = takeSpeech().lower()
            speak("Searching" + yt + " on YouTube for you")
            wb.open('https://www.youtube.com/results?search_query='+yt)

        # If User asks for a Joke
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        # If User wants to save a note
        elif 'take a note' in query:
            speak('What do you want me to note down?')
            notes = takeSpeech()
            # The note will be Saved in a Notes.txt text file
            f = open('Notes.txt', 'w')
            f.write(notes)
            speak('Saved!')

        # If User wants to View the Saved Notes
        elif 'show notes' in query:
            speak('Displaying your Latest Note')
            f = open('notes.txt', 'r')
            print(f.read())
            speak(f.read())

        # If User wants to take a screenshot
        elif 'screenshot' in query:
            img = pyautogui.screenshot()
            img.save('G:\Python Projects\RAJ-The_AI_Assistant\screenshots\ss.png')

        # It is a Exit/Stop Function
        elif 'exit' or 'thank you' in query:
            # The fucntion greets the User GoodBye
            speak("Thank you for Using RAJ AI Assistant.")
            speak("Have a Good Day Sir!")
            print("Thank You!")
            quit()

        # If User asks to Remember Something
        elif 'remember that' in query:
            speak("What do you want me to Remember?")
            memory = takeSpeech()
            speak("You asked me to Remember that " + memory)
            # It is Saved in a Memory.txt Text file
            remember = open('Memory.txt', 'w')
            remember.close

        # If User Wants to View Memory.txt
        elif 'remember anything' in query:
            remember = open('Memory.txt', 'r')
            speak("You asked me to Remember that " + remember.read())

        # If User wants to Know the Current TechCrunch News Headlines
        elif 'news' in query:
            try:
                jsonObj = urlopen(
                    "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=17dac822801d4f5a8be7471d5cba1bf4")
                data = json.loads(jsonObj)
                i = 1
                speak("Here are some top Headlines from TechCrunch")
                for item in data['articles']:
                    print(str(i) + '. '+item['title'] + '\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        # If User wants to know a Location on Google Maps
        elif 'where is' in query:
            query = query.replace('where is', '')
            loc = query
            speak('Locating' + loc + 'for you')
            wb.open_new_tab('https://www.google.com/maps/place/' + loc)

        # ToDo ---- Add Calculator Function

        # ToDo ---- Add Asking Questions (Definitions)

        # ToDo ---- Add Music Function

        # If User wants RAJ to Stop Listening for input seconds
        elif 'stop listening' in query:
            speak("For how long do you want me to stop listening?")
            ans = int(takeSpeech())
            time.sleep(ans)
            print(ans)

        # If User wants to Log Out
        elif 'log out' in query:
            os.system("shutdown -1")

        # If User wants to Restart System
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        # If User wants to Shutdown the System
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        # More Functions to Be Added in Future Updates
