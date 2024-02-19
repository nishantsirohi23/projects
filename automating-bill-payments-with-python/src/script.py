from lib2to3.pgen2 import driver
import tkinter as tk
import tkinter.messagebox
import bs4,time,requests
from numpy import take
#all the modules to be imported
from multiprocessing.connection import wait
from time import sleep
import pyttsx3
import scipy as sp
import speech_recognition as sr 
import pyaudio
import datetime
import webbrowser
import requests
import pywhatkit
import os
#from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from tkinter import *
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   '''def save(self):
       n=name.get()
       print(n)'''
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
       self.name=tk.StringVar()
       self.mail=tk.StringVar()
       self.phn=tk.StringVar()
       frame2=tk.Frame(self,bg="lightblue",width=1200,height=700)
       frame2.pack()
       lname=tk.Label(frame2,bg="lightblue",text="Name:")
       lname.pack()
       lname.place(x=180,y=0)
       entry=tk.Entry(frame2,textvariable=self.name)
       entry.pack()
       entry.place(x=150,y=30)
       lmail=tk.Label(frame2,bg="lightblue",text="E-Mail Id:")
       lmail.pack()
       lmail.place(x=180,y=60)
       email=tk.Entry(frame2,textvariable=self.mail)
       email.pack()
       email.place(x=150,y=90)
       lphn=tk.Label(frame2,bg="lightblue",text="Phone no.:")
       lphn.pack()
       lphn.place(x=180,y=120)
       ephn=tk.Entry(frame2,textvariable=self.phn)
       ephn.pack()
       ephn.place(x=150,y=150)
       def save():
           n=self.name.get()
           m=self.mail.get()
           p=self.phn.get()
           print(n,"\n",m,"\n",p)
           entry.delete(0, 'end')
           email.delete(0, 'end')
           ephn.delete(0, 'end')
       sav_bn=tk.Button(frame2,bg="lightblue",text="OK",command=save)
       sav_bn.pack()
       sav_bn.place(x=195,y=180)
       label = tk.Label(frame2,bg="lightblue", text="Fill your details")
       
       label.pack(side="top", fill="both", expand=True)
       label.place(x=170,y=270)
       
       
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #label = tk.Label(self, text="This is page 2")
       frame1=tk.Frame(self,bg="lightblue",width=1200,height=700)
       frame1.pack()
       #bslabel=tk.Label(frame1, text="BSNL Bill Payment - ",font=("BOLD", 15),bg="lightblue")#,padx=200,pady=200)
       #bslabel.pack()
       #bslabel.place(x=50,y=60)
       def bsnl1call():
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
        #speak("aa")
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
                elif "temp" in query or "temperory" in query:
                    driver = webdriver.Chrome('/Users/nishantsirohi/Downloads/chromedriver')
                    driver.get("https://temp-mail.org/en/")

                    sleep(3)
                    element = driver.find_element_by_id("mail")
                    val = element.get_attribute("value")
                    speak("I got a temperory email")
                    print(val)
                    speak("do you want to close this website")
                    task = takeCommand()
                    if "yes" in task or "yeah" in task or "sure" in task:
                        driver.close()
                    

                
                elif "search" in query:
                    query = query.replace("search","")
                    if (len(query) == 0):
                        speak("what do you want to search")
                        search_str = takeCommand()
                        driver = webdriver.Chrome('/Users/nishantsirohi/Downloads/chromedriver')
                        driver.get("https://www.google.com")
                        element = driver.find_element_by_name("q").send_keys(search_str)
                        button = driver.find_element_by_name("btnK").click()
                    else:
                        driver = webdriver.Chrome('/Users/nishantsirohi/Downloads/chromedriver')
                        driver.get("https://www.google.com")
                        element = driver.find_element_by_name("q").send_keys(query)
                        button = driver.find_element_by_name("btnK").click()

                elif "download" in query:
                    speak("which image you want to download")
                    os.system('python facebook_login.py')
            
                print(query)
        
        

        




          
        
           
       photo=tk.PhotoImage(file="/Users/nishantsirohi/codes/automating-bill-payments-with-python/src/bsnllogo.png")
       #photo = photo.resize((25, 25), Image.ANTIALIAS) #The (250, 250) is (height, width)
       #self.pw.pic = ImageTk.PhotoImage(photo)
       #scale_w = new_width/old_width
       #scale_h = new_height/old_height
       #photo.zoom(.01, .01)
       bsbutton=tk.Button(frame1,image=photo,command=bsnl1call,)#height=50,width=50,text="Click Here",font=("BOLD", 10))
       bsbutton.image=photo
       bsbutton.pack()#**button_opt)
       bsbutton.place(x=50,y=60)
       #elabel=tk.Label(frame1,text="Electricity Bill Payment - ",font=("BOLD", 15),bg="lightblue")
       #elabel.pack()
       #elabel.place(x=50,y=180)
       def electpay():
           def autofill():
            select=Select(browser.find_element_by_name('circle'))
            select.select_by_visible_text('RANGAREDDY')
            select=Select(browser.find_element_by_name('ero'))
            select.select_by_visible_text('SAROORNAGAR')
            eleid=browser.find_element_by_name('sno')
            eleid.send_keys('1574 15192')
            eleid=browser.find_element_by_name('makePayment')
            eleid.click()

           def pay():
            sub=browser.find_element_by_name("button2")
            sub.click()
            time.sleep(1)
            element=browser.find_element_by_id('cnumber')
            element.send_keys('4373-7820-1028-0000')
            select=Select(browser.find_element_by_name('expmon'))
            select.select_by_visible_text('05 (May)')
            select=Select(browser.find_element_by_name('expyr'))
            select.select_by_visible_text('2020')
            element=browser.find_element_by_id('cvv2')
            element.send_keys('684')
            element=browser.find_element_by_id('cname2')
            element.send_keys('LAKSHMA REDDY B')
           browser=webdriver.Chrome('C:\DRIVERS\CHROMEDRIVER\chromedriver.exe')
           browser.get('https://www.billdesk.com/APCPDCL/apcpdcl.htm')
           autofill()
           time.sleep(4)
           bill=browser.find_element_by_name("txtTxnAmount")
           amt=bill.get_attribute("value")
           #print('Your electricity bill for current month is ',amt)
           due=browser.find_element_by_name("due_date")
           date=due.get_attribute("value")
           #print('You should pay by: ',date)
           #ch=input("\nDo you want to proceed to payment? Y/N ")
           answer=tkinter.messagebox.askquestion("Details","Your electricity bill for current month is"+amt+"\nYou should pay by:"+date+"\nDo you want to proceed to payment?")
           if answer=='yes':
               pay()
               #print('Do you want to confirm payment of Rs.',amt,'? Y/N')
               answer=tkinter.messagebox.askquestion("Want to make payment?","Do you want to confirm payment of Rs."+amt+"?")
               #ch=input()
               if answer=='Y':
                   element=browser.find_element_by_id('proceedForm')
                   element.click()
               else:
                   time.sleep(2)
                   browser.quit()
                   #element=browser.find_element_by_link_text('Cancel')
                   #element.click()
    
           else:
                browser.quit()


       photo2=tk.PhotoImage(file="/Users/nishantsirohi/codes/automating-bill-payments-with-python/src/elec-logo.png")
       ebutton=tk.Button(frame1,image=photo2,command=electpay)#text="Click here",font=("ITALIC", 10)
       ebutton.image=photo2
       ebutton.pack()
       ebutton.place(x=250,y=60)
       
       #label.pack(side="top", fill="both", expand=True)
           

class Page3(Page):
  def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       frame3=tk.Frame(self,bg="lightblue",width=1200,height=700)
       frame3.pack()
       label = tk.Label(frame3,bg="lightblue",font=("BOLD",11), text="About: Automate your bill payments with this application \n    Save your details and run the app to pay bills. \t\t\n\n\nDeveloped by:\t\t\t\t\t\nB.Abhinandan\t\t\t\t\nS.Ikshwak\t\t\t\t\nT.Abhishek\t\t\t\t\t")
       
       label.pack(side="top", fill="both", expand=True)
       label.place(x=10,y=10)

class MainView(tk.Frame):
  def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #self.configure(background='lightblue')
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Add Details", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Home", command=p2.lift)
        b3 = tk.Button(buttonframe, text="About", command=p3.lift)

        b2.pack(side="left")
        b1.pack(side="left")
        b3.pack(side="left")

        p2.show()


if __name__ == "__main__":
    root = tk.Tk()#.config(bg="lightblue")
    #root["bg"] = "lightblue"
    
    main = MainView(root)
    
    main.pack(side="top", fill="both", expand=True)
    #main.option_add("*background", "lightblue")
    root.title("Automating Bill Payments")
    #root.configure(background='lightblue')
    root.wm_geometry("400x400")
    root.mainloop()
