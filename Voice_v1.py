import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import subprocess as sp


# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

    
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Ayesha. How can I help you.")

def greetAgain():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        exit_command = False 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please say that again...")
        return None

    return query




def open_camera():
    speak(f"Camera Openning!!! Sir please take some good pictures.")
    sp.run('start microsoft.windows.camera:', shell=True)

def open_xampp():
    #sp.run('start xampp-control.exe', shell=True)

    os.startfile(r"C:\xampp\xampp-control.exe")

def open_cmd():
    os.system('start cmd')

def search_on_google(query):
    sp.search(query)

#def search_chrome():
#    query = listen().lower()
    

def process_q(query):
    if 'hi ayesha' in query.lower():
        speak("Hi sir")
    elif 'ayesha wake up' in query.lower():
        speak("I am awake sir")
    elif 'i am doing good how are you' in query.lower():
        speak('I am feeling good. Thanks for asking.')
        speak('How can I help you today.')
    elif 'check for new updates in the system' in query.lower():
        speak("Give me a moment to check.")
        speak("")
        speak("Sir, looks like you dont have any new update.")
        speak("If any update will come I will ping you back.")
    elif 'thanks' in query.lower():
        speak("No worries sir, it's my job to keep you updated.")
    elif 'what happened' in query.lower():
        speak("Nothing just trying to understand what I missed.")
    elif 'do you know me' in query.lower():
        speak("Looks like I heared your voice somewhere.")
    elif 'where did you heard' in query.lower():
        speak("Not sure sir, I am looking into my memory")
    elif 'what is the issue' in query.lower():
        speak("Not able to identify the issue but it looks like some backend issue")
    elif 'are you sure' in query.lower():
        speak("According to my logical calculation it seems like I am correct.")
        speak("But still I will recheck to be sure.")
    elif 'open google' in query.lower():
        webbrowser.open("https://www.google.com")
    elif 'open git' in query.lower():
        webbrowser.open("https://www.github.com/")
    elif 'current time' in query.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'open camera' in query.lower():
        open_camera()
    elif 'open command' in query.lower():
        open_cmd()
    elif 'open server' in query.lower():
        open_xampp()
    #elif 'search google' in query.lower():
    #    search_chrome()
#    elif 'sleep now':
#       speak("Ok sir, please wake me up if you need any more assistance.")
    elif 'shiv' in query.lower():
        speak('yes')
        speak('should i receite it for you')
    elif 'yes' in query.lower():
        speak("Jatatavi galajjala pravahapavi tasthale Galeavalambya lambitam bhujanga tunga malikam Damad damad damad dama ninad ava damarvayam Chakara chand tandavam tano tunah shivah shivam")
        speak("Jata kata hasambhrama bhramani limpanirjhari Vilolavi chivalarai virajaman amurdhani Dhaga dhagadh agajjva lalalata patta pavake Kishora chandra shekhare ratih pratikshanam mama")
    else:
        speak("I'm sorry")
        speak("I am not able to hear you properly.")

     # elif 'search on google' in query.lower():
#     #         speak('What do you want to search on Google, sir?')
#     #         query = listen().lower()
#     #         search_on_google(query)


if __name__ == "__main__":
    greet()
    while True:
        query = listen()
        if query:
            process_q(query)

