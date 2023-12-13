import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import subprocess
import datetime
import os
import time
import cv2
import random2
from requests import get
import wikipedia
import webbrowser
from time import sleep
import sys
import pyjokes
import smtplib
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import winshell
from twilio.rest import Client





engine = pyttsx3. init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id
engine.setProperty('voices', voices[0].id)

mozila_path='"C:\\Program Files\\Mozilla Firefox\\firefox.exe" %s'

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def  takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=30)

    try:
            print("recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

    except Exception as e:
        speak("Sorry i can't hear can you please speak that again")
        return"none"
    for a in range(3):
        if a<3:
            return query

#for news headlines
def news():
    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    newslimit=5
    # read news title
    for news in news_list:
        speak(news.title.text)
        print(news.title.text)
        print("-"*60)
        newslimit=newslimit-1
        if newslimit==0:
            return


#To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")


    else:
        speak("good evening")
    speak("hello i am jarvis, how can i help you")

#to send email
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.ehlo()
    server.login('harshit.chourishiya2020@vitbhopal.ac.in', '[#chuchu007]')
    server.sendmail('harshit.chourishiya2020@vitbhopal.ac.in', to, content)
    server.close



if __name__ == '__main__':
    wish()
    while True:


        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
                speak("opening notepad")
                location = "C:/WINDOWS/system32/notepad.exe"
                notepad = subprocess.Popen(location)

        elif "close notepad" in query:
                speak("closing notepad")
                notepad.terminate()

        elif "open after burner" in query:
            apath = "C:\\Program Files (x86)\\MSI Afterburner\\msiafterburner.exe"
            speak("ok wait a moment i am opening msi after burner")
            burner = subprocess.Popen(apath)

        elif "close after burner" in query:
            speak("closing msi after burner")
            location="C:\\Program Files (x86)\\MSI Afterburner\\msiafterburner.exe"
            burner.terminate()

        elif ("open ms word") in query:
            speak("opening ms word")
            location="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            word=subprocess.Popen(location)

        elif ("close ms word") in query:
            speak("closing ms word")
            word.terminate()

        elif ("open ms word") in query:
            speak("opening ms word")
            location="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            word=subprocess.Popen(location)

        elif "open command prompt" in query:
            speak("ok wait a moment i am opening command prompt")
            os.system("start cmd")

        elif "open camera" in query:
            speak("ok i am opening camera and you make sure that you'r looking osm for a shoot")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)   
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            speak("ok i am playing music to freshup your mood")
            music_dir = "C:\\Users\\Admin\\Music"
            songs = os.listdir(music_dir)
            #rd = random2.choice(songs)
            for song in songs:
                if song.endswith(''):
                    os.startfile(os.path.join(music_dir, song))
            break

        elif "what is the time now" in query:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)
            speak(f"the time is {current_time}")


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")


        elif "wikipedia" in query:
            speak("searching from wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            speak("ok fine i am opening youtube...")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            query = query.replace("open youtube","")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("done")
            break

         
        elif "search" in query:
            if len(query)==6:
                speak("what should i search")
                query=takecommand().lower()
                x=query.split()
                web="https://www.google.com/search?client=firefox-b-d&q="
                for a in x:
                    web=web+"+"+a

                webbrowser.get(mozila_path).open_new_tab(web)

            else:
                query = query.replace("search", "")
                x=query.split()
                web="https://www.google.com/search?client=firefox-b-d&q="
                for a in x:
                    web=web+"+"+a

                webbrowser.get(mozila_path).open_new_tab(web)


        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow, Happy coding")
            webbrowser.get(mozila_path).open("stackoverflow.com")

        elif "open google" in query:
            speak("ok what would you like to search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")


        elif 'news' in query:
            news()
             
            
        elif "whatsapp message" in query:
            speak("tell me the phone number")
            phone = takecommand()
            ph = '+91' + phone
            speak("tell me the message")
            msg = takecommand()
            speak("tell me the time")
            speak("time in hour")
            hour = int(takecommand())
            speak("time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            speak("ok sending whatsapp message")

        elif "joke" in query:
            a=random2.choice(pyjokes.get_jokes())
            speak(a)


        
        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
             speak('restarting in 5 second')
             sleep(5)
             os.system("shutdown /r /t 1")

        elif "email to harshit" in query:
            try:
                speak("what should i say")
                content=takecommand().lower()
                to="harshit@gmail.com"
                sendemail(to, content)
                speak("email has been sent to harshit")

            except Exception as e:
                print(e)
                speak("sorry sir i cant able to send this email")

        elif "email to harshit goswami" in query:
            try:
                speak("what should i say")
                content=takecommand().lower()
                to=("harshit.goswami@vitbhopal.ac.in")
                sendemail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry sir i cant able to send this email")

        elif "email to divyansh" in query:
            try:
                speak("what should i say")
                content=takecommand().lower()
                to=("divyansh.mittal@vitbhopal.ac.in")
                sendemail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry sir i cant able to send this email")

        elif "email to paras sir" in query:
            try:
                speak("what should i say")
                content=takecommand().lower()
                to="paras.jain@vitbhopal.ac.in"
                sendemail(to,content)
                speak("email has been sent sir")

            except Exception as e:
                print(e)
                speak("sorry sir i cant able to send this email")

        elif "send email" in query:
            try:
                speak("what should i say")
                content=takecommand().lower()
                speak("whom should i send sir please type")
                to=input(str("type email id"))
                sendemail(to,content)
                speak("email has been sent sir")

            except Exception as e:
                print(e)
                speak("sorry sir i cant send this mail")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"")

        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "93a80005c31cd8ef59c11ad2d32fe8f1"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            city_name=takecommand()
            complete_url = (base_url+"appid="+api_key+"&q="+city_name)
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = round(y["temp"] -273.15)
                current_pressure = y["pressure"] * 0.0295
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print("current Temperature in" + city_name +" is" + str(current_temperature)+ " degree celcius " + " \n atmospheric pressure in"+ city_name+ " is" + str(current_pressure)+" inches of mercury" + " \n humidity in"+ city_name+ " is"+ str(current_humidiy)+" percent" + " the weather in" + city_name + " will be" + str(weather_description))
                speak("current Temperature in" + city_name +" is" + str(current_temperature)+ " degree celcius " + " \n atmospheric pressure in"+ city_name+ " is" + str(current_pressure)+" inches of mercury" + " \n humidity in"+ city_name+ " is"+ str(current_humidiy)+" percent" + " the weather in" + city_name + " will be" + str(weather_description))
             
            else:
                speak(" City Not Found ")

        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'AH8q3dGK2f2vLZVgbRfLTjQPySe2yRaJHs'
                auth_token = '152b437a0bb91a115d0485a248290822s'
                client=Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takecommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
		
                print(message.sid)

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak("note has been saved sir")
            else:
                file.write(note)
                speak("notes has been saved sir")
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))


        elif ("how are you jarvis") in query:
            speak("i am fine what about you")

        elif ("i like your name jarvis") in query:
            speak("thanks that's so nice to hear")

        elif ("do you like your name") in query:
            speak("yes i like my name very much")

        elif ("who makes you") in query:
            speak("i was made by a team of some students from V I T institute ")

        elif ("what is your working") in query:
            speak("i work similar as google assistant but i have a speacial characteristic that i can work on offline mode to make it convenient and easier for you")

        elif ("hello jarvis") in query:
            speak("hey nice to hear your voice hows your day")

        elif ("what is your name") in query:
            speak("Did I forget to introduce myself")
            speak("I am your jarvis, personal assistant")

        elif ("your birthday") in query:
            speak("I try to live every day like its my birthday ,I get more cake that way")

        elif ("are you a robot") in query:
            speak("I would prefer to think of myself as your friend, Who also happens to be artificially intelligent")

        elif ("what about yours day how is it") in query:
            speak("its splendid that i am talking to you let me know if there is anything i can do for you")

        elif ("goodbye" in query):
            print("Thanks For Your Time, GoodBye!")
            speak("Thanks For Your Time, Good Bye!")
            sys.exit()

