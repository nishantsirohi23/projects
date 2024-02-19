#all the modules to be imported
from multiprocessing.connection import wait
from time import sleep
import pyttsx3
import speech_recognition as sr 
import pyaudio
import datetime
import webbrowser
import pywhatkit
import os


#intializing the engine (for speech)
engine = pyttsx3.init() 
voices = engine.getProperty('voices') 
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)
engine.setProperty('voice', voices[0].id) 


#function to speak the text
def speak(audio): 
    engine.say(audio) 
    engine.runAndWait()

def createFile(path,filename):
    name = "user"+'/'+filename  # Name of text file coerced with +.txt 
    try:
        file = open(name,'a')   # Trying to create a new file or open one
        file.close()
    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python    

  
#funcition to take username
def username(): 
    speak("What should i call you sir") 
    uname = takeCommand() 
    speak("Welcome Mister") 
    speak(uname)  
    speak("How can i Help you, Sir") 

#function to take command fom user
def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        #speak("Listening") 
        print("Listening")
        r.pause_threshold = 0.5
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to Recognizing your voice.")   
        return "None"
      
    return query 



if __name__ == '__main__': 
   
    
    assname =("Jarvis 1 point o") 
    

    #do the command as said by the user
    while True: 
          
        query = takeCommand().lower() 
        #print(query)
        if "whatsapp" in query:
            print("what is the message you want to send")
            sleep(1)
            message = takeCommand()
            pywhatkit.sendwhatmsg("+919084940146", message,16,55)

        elif 'instagram' in query:
            print("user want to open instagram")
            webbrowser.open("https://www.instagram.com")

        elif "gmail" in query:
            print("user want to open gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'play' in query: 
            query = query.replace("play", "")      
            #print(query)     
            pywhatkit.playonyt(query)
             
        
        elif 'youtube'  in query:
            print("what you want to search on youtube")
            search_str = takeCommand()
            pywhatkit.playonyt(search_str)
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
        
            
        print(query)
          
        