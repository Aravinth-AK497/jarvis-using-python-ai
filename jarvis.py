import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)

def engine_talk(voice):
    print(f"Jarvis is saying: {voice}")
    engine.say(voice)
    engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            engine_talk("I AM JARVIS HOW CAN I HEPL YOU!")
            print("I AM JARVIS HOW CAN I HEPL YOU!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(f"User said: {command}")
                return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
    except sr.RequestError:
        print("Could not request results; check your network connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return ""

def run_jarvis():
    command = user_commands()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            engine_talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            engine_talk('The current time is ' + time)
        elif 'who is' in command:
            name = command.replace('who is', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'joke' in command:
            engine_talk(pyjokes.get_joke())
        elif 'stop' in command:
            engine_talk('Goodbye!')
            sys.exit()
        else:
            engine_talk('I could not hear you properly')
    else:
        engine_talk('I did not catch that. Please speak again.')

while True:
    run_jarvis()
