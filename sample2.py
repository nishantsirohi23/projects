
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
#import winsound
#import winshell 
import requests
import pyjokes 
#import feedparser 
import smtplib 
import pyttsx3 
import time 
import requests 
import shutil 
from selenium import webdriver
#from twilio.rest import Client 
#from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
#import win32com.client as wincl 
#from urllib.request import urlopen
#from geopy.geocoders import Nominatim
#from geopy.distance import geodesic
#import gmaps 
import pywhatkit 


engine = pyttsx3.init() 
voices = engine.getProperty('voices') 
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)
engine.setProperty('voice', voices[0].id) 

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Jarvis 2 point o") 
    speak("I am your Assistant and I am created by Nishant Sirohi") 
    speak(datetime.datetime.now().time())
    speak(assname) 
    username()
      
  
def username(): 
    speak("What should i call you sir") 
    uname = takeCommand() 
    speak("Welcome Mister") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("#####################".center(columns)) 
    print("Welcome Mr.", uname.center(columns)) 
    print("#####################".center(columns)) 
      
    speak("How can i Help you, Sir") 
  
def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
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
   
def sendEmail(to, content): 
    server = smtplib.SMTP('nishantsirohi2307@gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    # Enable low security in gmail 
    server.login('your email id', 'your email passowrd') 
    server.sendmail('your email id', to, content) 
    server.close()
def search1(text):
    import pywhatkit as kit1
    kit1.info("Python",lines=3,speak=None)
    

    

    
    
    
    
    
    
if __name__ == '__main__': 
    clear = lambda: os.system('clear') 
       
      
    # This Function will clean any 
    # command before execution of this python file 
    clear() 
    username() 
    takeCommand()
    assname =("Jarvis 1 point o") 
      
    while True: 
          
        query = takeCommand().lower() 
          
        # All the commands said by user will be  
        # stored here in 'query' and will be 
        # converted to lower case for easily  
        # recognition of command 
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 2) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
  
        elif 'open youtube' in query: 
            speak("Here you go to Youtube\n") 
            webbrowser.open("youtube.com")
            
        elif 'play song on youtube' in query:
            speak("which song do you wnat to play\n")
            song = takeCommand()
            print(song)
        elif 'birthday song for lovely' in query:
            speak("Happy Birthday to You, cha, cha, cha Happy Birthday to You, cha, cha, cha.  Happy Birthday Dear lovely  Happy Birthday to You, cha, cha, cha.")
                 
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        
        elif 'notepad' in query:
            notepath =  r"C:\Users\Nishant Sirohi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories"
            speak("Here you go to Noteopad")
            os.startfile(notepath)
            
        elif 'youtube' in query:
            speak("please tell the name of the video")
            video = takeCommand()
            pywhatkit.playonyt(video)
            
            
        elif 'whatsapp' in query:
            bro = "+918630277749"
            papaji = "+916005508409"
            chacha = "+917027319519"
            speak("Please tell whom you wnat to send the message")
            print("Please tell whom you wnat to send the message")
            name = takeCommand()
            if(name == bro or name == papaji or name == chacha):
                speak("please tell the message you want to send")
                print("please tell th meassage you want to send")
                mes = takeCommand()
                speak("Tell the hour at which you want to send the message")
                print("Tell the hour at which you want to send the message")
                hour = takeCommand()
                speak("Tell the minute at which you want to send the message")
                print("Tell the minute at which you want to send the message")
                min = takeCommand()
                pywhatkit.sendwhatmsg(name , mes , hour , min) 
            else:
                speak("Type the number")
                print("Type the number")
                name = takeCommand()
                speak("please tell the message you want to send")
                print("please tell th meassage you want to send")
                mes = takeCommand()
                speak("Tell the hour at which you want to send the message")
                print("Tell the hour at which you want to send the message")
                hour = takeCommand()
                speak("Tell the minute at which you want to send the message")
                print("Tell the minute at which you want to send the message")
                min = takeCommand()
                pywhatkit.sendwhatmsg(name , mes , hour , min) 
                
                
                
            
        elif 'open google' in query: 
            speak("Here you go to Google\n") 
            webbrowser.open("google.com") 
  
        elif 'open stackoverflow' in query: 
            speak("Here you go to Stack Over flow.Happy coding") 
            webbrowser.open("stackoverflow.com")    
  
        elif 'play music' in query or "play song" in query: 
            speak("Here you go with music") 
            
            music_dir = "C:\\Users\\Nishant Sirohi\Desktop\music"
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[1])) 
  
        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("% H:% M:% S")     
            speak(f"Sir, the time is {strTime}") 
  
        elif 'open opera' in query: 
            codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath) 
        
     
            
               
            
            
  
        elif 'email to Nishant' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                to = "Receiver email address"    
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'send a mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("whome should i send") 
                to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
  
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  
        elif "change name" in query: 
            speak("What would you like to call me, Sir ") 
            assname = takeCommand() 
            speak("Thanks for naming me") 
  
        elif "what's your name" in query or "What is your name" in query: 
            speak("My friends call me") 
            speak(assname) 
            print("My friends call me", assname) 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit
  
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by Gaurav.") 
              
        elif 'joke' in query: 
            speak(pyjokes.get_joke()) 
              
       
  
        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
  
        elif "who i am" in query: 
            speak("If you talk then definately your human.") 
  
        elif "why you came to world" in query: 
            speak("Thanks to Gaurav. further It's a secret") 
  
        elif 'virtual box' in query: 
            speak("opening Oracle VM Virtual Box") 
            power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Oracle VM VirtualBox\Oracle VM VirtualBox.exe"
            os.startfile(power) 
  
        elif 'is love' in query: 
            speak("It is 7th sense that destroy all other senses") 
  
        elif "who are you" in query: 
            speak("I am your virtual assistant created by Nishant Sirohi") 
  
        elif 'reason for you' in query: 
            speak("I was created as a Minor project by Nishant sirohi ") 
  
       
        elif 'open bluestack' in query: 
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli) 
  
       
       
  
       
                  
        
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
  
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
        elif "timer" in query:
            speak("Please tell time in seconds")
            a = int(takeCommand())
            time.sleep(a)
            fr = 100
            dura = 5000
           
            
  
  
        
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
                speak("Notes saved successfully")
            else: 
                file.write(note) 
                speak("Notes saved successfully")
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
  
       
        elif "jarvis" in query: 
              
            wishMe() 
            speak("Jarvis 2 point o in your service Mister") 
            speak(assname) 
  
        elif "weather" in query: 
              
            # Google Open weather website 
            # to get API of Open weather  
            api_key = "AIzaSyCpJL1CQfOvORdRf0Aagn4bH1IhAClbfAA" 
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
              
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
              
            else:  
                speak(" City Not Found ") 
              
        
  
  
        elif "wikipedia" in query: 
            webbrowser.open("wikipedia.com") 
  
        elif "Good Morning" in query: 
            speak("A warm" +query) 
            speak("How are you Mister") 
            speak(assname) 
  
        # most asked question from google Assistant 
        elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm not sure about, may be you should give me some time") 
  
        elif "how are you" in query: 
            speak("I'm fine, glad you me that") 
  
        elif "i love you" in query: 
            speak("It's hard to understand") 
  
        