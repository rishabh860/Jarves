import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
# sapi5 - SAPI5 on Windows
# nsss - NSSpeechSynthesizer on Mac OS X
# espeak - eSpeak on every other platform
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

email = "email"
password = "password"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if(hour > 0 and hour < 12):
        speak("Good Morning Rishabh....")
    elif(hour >= 12 and hour < 16):
        speak("Good Afternoon Rishabh...")
    elif(hour >= 16 and hour < 19 ):
        speak("Good Evening Rishabh...")
    else:
        speak("Good Night Rishabh...")
    
    speak("Hello Rishabh, im your Assistent , How May I help You Today....")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recorganising what you just said...")
        query = r.recognize_google(audio, language = "en-in")
        print(f"You just spock {query} \n")
    
    except Exception as e:
        print("Voice wasn't clear, can you repeat what you said again...")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    # speak("hey how are you..")
    wishme()
    while True:

        query = listen().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query:
            speak("Opening youtube please wait..")
            webbrowser.open("youtube.com")
        
        elif "open facebook" in query:
            speak("Opining your facebook..")
            webbrowser.open("facebook.com")

        elif "open netflix" in query:
            speak("Opining netflix")
            webbrowser.open("netflix.com")

        elif "play music" in query:
            import random
            speak("Opening your music directry please wait a sec...")
            music_dir = 'R:\\series\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs.randrange(0, (len(songs)-1))))

        elif "shutdown" in query:
            speak("Shutting down your pc..")
            os.system("shutdown /s /t 1")
        
        elif 'email to rishabh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "krrishabh1402@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Rishabh. I am not able to send this email")   

        
