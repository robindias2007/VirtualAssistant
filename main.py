import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',120)
engine.setProperty('voice', voices[10].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            else:
                print("You didnt say anything")
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'information' in command:
        person = command.replace('information', '')
        info = wikipedia.summary(person, 2)
        talk(info)
        print(info)
    elif 'are you single' in command:
        talk('Sorry iam in a relationship with WIFI')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please tell your command again. I did not understand')

# to keep on running
# while True:
#     run_alexa()

run_alexa()