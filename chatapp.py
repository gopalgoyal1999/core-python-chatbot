import os
import random
import pyttsx3
import webbrowser
import numpy as np
import pandas as pd
import bs4
import speech_recognition as sr
import urllib.request as url
from datetime import datetime
from mlchange import transp
from googletrans import Translator
trans =Translator()
en=pyttsx3.init('sapi5')
voices=en.getProperty('voices')
en.setProperty('voice',voices[1].id)   # 0 for male voice or 1 for female voice
hi=['hi','hello','hey','helloooo','hiiii']
bye=['bye','byeee']
news=['news','todays news','open news']
music=['music','song','play music','open music','songs']
movies=['movies','movie','play movie']
web=['google','search-engine','web-browser','web','web-explorer','open web']
li=[ 'movie' , 'song' , 'web-browser' , 'desktop' ,'google','songs','movies','news','todays news','open news','play music','open music','play movie','change','views','movie views','view','imdb']
l='movie,song,news,google,desktop,change,views'
n='news,today news, open news'
li1=['any song','random','play song']
change=['change']
view=['views','movie views','view','imdb']
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()
device_id = None

a=datetime.now()
print(a)
en.say("Namaste")
en.runAndWait()

def speech_to_text():
    print("Listening")
    audio = r.listen(source)
    print("Waiting for connection")
    option = r.recognize_google((audio) ,language='hi-IN')
    option = trans.translate(option,dest='en')
    option = option.text
    option = option.lower()
    print("you said: " + option)
    text_to_speech(option)
    return option

def speech():
    print("Listening")
    audio = r.listen(source)
    print("Waiting for connection")
    option = r.recognize_google(audio)
    option = option.lower()
    print("you said: " + option)
    text_to_speech(option)
    return option

def text_to_speech(a):
    en.say(a)
    en.runAndWait()
    print(a)

    
while True:

    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i

    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                            chunk_size = chunk_size) as source:

        r.adjust_for_ambient_noise(source)
        try:
            a = " Welcome  User "
            text_to_speech(a)
            choice=speech_to_text()
            if choice in hi:
                a = "How are u ?"
                text_to_speech(a)
                ch=speech_to_text()
                text_to_speech(" What can i help you ? ")
                text_to_speech(l)
                option = speech_to_text()
                if option not in li:
                    break
                '''print("Listening...")
                audio = r.listen(source)
                print("Waiting for connection")
                option = r.recognize_google(audio) #,language='hi-IN')
                option = option.lower()
                print("you said: " + option)
                en.say(option)
                en.runAndWait()'''

                if option in music:
                    os.chdir("E:/Pj_songs")
                    d=os.listdir()
                    for i in range(len(d)):
                        print(i+1," ",d[i])
                    b = "enter the music number you want to listen or random song "
                    text_to_speech(b)
                    number = speech_to_text()
                    if number in li1:
                        file = random.choice(d)
                        os.startfile(file)
                    else :
                        number = int(number)
                        file=d[number-1]
                        os.startfile(file)

                elif option in change:
                    transp()

                elif option in view:
                    path="https://www.imdb.com/"
                    http_response=url.urlopen(path)
                    webpage=bs4.BeautifulSoup(http_response,'lxml')
                    m = "enter the movie name"
                    text_to_speech(m)
                    movie_name=speech()
                    newpath=path+"find?ref_=nv_sr_fn&q="+movie_name
                    http_response=url.urlopen(newpath)
                    webpage1=bs4.BeautifulSoup(http_response)
                    data=webpage1.find('td',class_="result_text")
                    data1=data.find('a')['href']
                    newpath2=path+data1
                    http_response=url.urlopen(newpath2)
                    webpage2=bs4.BeautifulSoup(http_response,'lxml')
                    data=webpage2.find('div',class_="title_wrapper")
                    data1=data.find('h1')
                    data5=webpage2.find('div',id="titleDetails")
                    data2=webpage2.find('div',class_="plot_summary")
                    data3=webpage2.find('div',class_="user-comments")
                    view=data3.findAll('a')
                    print(view[-1])
                    data4=data3.find('p')
                    data6=webpage2.find('div',class_="title_block")
                    print(data1.text)
                    print(data2.text)
                    print(data6.text)
                    print(data4.text)

                    
                elif option == "desktop":
                    os.chdir("C:/Users/user/Desktop")
                    d=os.listdir()
                    for i in range(len(d)):
                        print(i+1," ",d[i])
                    a = "enter the number what you want to open"
                    text_to_speech(a)
                    number = speech_to_text()
                    number = int(number)
                    file=d[number-1]
                    os.startfile(file)
    

                elif option in movies:
                    os.chdir("e:/Music")
                    d=os.listdir()
                    for i in range(len(d)):
                        print(i+1," ",d[i])
                    a = "enter the movies number you want to listen "
                    text_to_speech(a)
                    number = speech_to_text()
                    number = int(number)
                    file=d[number-1]
                    os.startfile(file)
        
                elif option in news:
                    path="https://www.indiatvnews.com/"

                    http_response=url.urlopen(path)

                    webpage1=bs4.BeautifulSoup(http_response,'lxml')

                    News = "FYI,INDIA,WORLD,BUSINESS,SPORTS,SCIENCE,CRIME,JOB,POLITICS,ENTERTAINMENT,EDUCATION,LIFESTYLE "

                    news=['fyi','india','world','science','politics','education','business','jobs']
                    text_to_speech(News)

                    c= True

                    def loop(data):
                        '''a = "Do you want to listen all news (yes/no) ?"
                        text_to_speech(a)
                        ch = speech_to_text()
                        if ch=="yes":'''
                        for i in range(0,len(data)):
                            a=data[i].text
                            print(i+1,a)
                            text_to_speech(a)
                            print("  "*20)
                        print("*"*20)
                        '''else:
                            a = "tell me the number"
                            text_to_speech(a)
                            ch = speech_to_text()
                            ch = int(ch)
                            for i in range(0,len(data)):
                                a=data[i].text
                                text_to_speech(a)
                                if i==ch:
                                    break'''
    
  
                    while c:
                        a = " Enter the news type :   "
                        text_to_speech(a)
                        News_name=speech_to_text()

                        News_name=News_name.lower()

                        if News_name=='bye':
                            print("      THANKS      ")
                            c=False
                            break

                        newpath=path+News_name

                        http_response=url.urlopen(newpath)

                        webpage2=bs4.BeautifulSoup(http_response,'lxml')
    
        
                        if News_name in news :

                            page=webpage2.find('div',class_="big-news-list")

                            data=page.findAll('a')

                            print(News_name+"  News  ")
                            loop(data)

                        print("  LATEST NEWS  ")
                        page1=webpage2.findAll('ul',class_="list")
                        for i in range(0,len(page1)):
                            data=page1[i].findAll('p',class_="titel")
                            loop(data)
                        print("*"*20)


                        data=webpage2.findAll('p',class_="title")
                        loop(data)
    
                        print(" MORE NEWS")
                        page2=webpage2.findAll('div',class_="content")
                        for i in range(0,len(page2)):
                            data=page2[i].find('a',)
                            print(i+1,data.text)
                            print("  "*20)
                        print("*"*20)

                        print(" TOP NEWS ")
                        page1=webpage2.find('ul',class_="rhs_story")
                        data=page1.findAll('p',class_="title")
                        loop(data)
                elif option in web :

                    a = "do u want to to open google home page ? (yes/no)"
                    text_to_speech(a)
                    c=speech_to_text()
                    if c=='yes' :
                        webbrowser.open("www.google.com")
                    else:
                        a = "enter the name of website do you want to open"
                        text_to_speech(a)
                        site=speech_to_text()
                        if site == "youtube":
                            a = "enter the name of song do you want to open"
                            text_to_speech(a)
                            song = speech_to_text()
                            song = song.replace(" ","+")
                            webbrowser.open("https://www.youtube.com/results?search_query="+song)
                        else :
                            site=site.replace(" ","+")
                            webbrowser.open("https://www.google.com/search?q="+site)
                    
                else :
                    print("  BYE  ")
                break

        except BaseException as e:
            print(e)
