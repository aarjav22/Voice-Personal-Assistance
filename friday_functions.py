#reminder ka dalna he
#play music
#current location
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
from googlesearch import search
from PyDictionary import PyDictionary
import os
from youtube_search import YoutubeSearch
import requests
import json
import vlc
import pafy

def engine_init():
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    return engine

def speak(text,engine):
    engine.say(text)
    engine.runAndWait()

def welcome(engine):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello, Good Morning",engine)
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon",engine)
    else:
        speak("Hello, Good Evening",engine)

    speak("I am prabhu ,Your personal assistance?",engine)

def record(engine):
	r=sr.Recognizer()
	mic=sr.Microphone(device_index=1)

	with mic as source:
		print("listeninig....")
		r.adjust_for_ambient_noise(source,duration=1)
		audio=r.listen(source)

	try:
		print("recognizing....")
		query=r.recognize_google(audio)

	except Exception:
		speak("sorry sir not able to recognize plaease pardon",engine)
		return "None"
	return query

def search_wikipedia(query,engine):
    query=query.replace("wikipedia","")
    query=query.replace("wiki","")
    query=query.replace("who is","")
    query=query.replace("what is","")
    try:
        result=wikipedia.summary(query,sentences=1)
        speak("according to wikipedia",engine)
        speak(result,engine)
    except Exception as e:
        speak("Unable to complete your request please try again",engine)

def play_song(query,engine):
    query=query.replace('on','')
    query=query.replace('any','')
    query=query.replace('some','')
    query=query.replace('random','')

    result = YoutubeSearch(query, max_results=1).to_dict()[0]['id']
    url=f"https://www.youtube.com/watch?v="+result
    video=pafy.new(url)
    audiostreams=video.audiostreams
    song=audiostreams[0]
    song.download("temp."+song.extension)
    speak("Playing Song",engine)
    player = vlc.MediaPlayer("./temp."+song.extension)
    player.play()
    return True,player,song

def open_google(query,engine):
    query=query.replace('open','')
    query=query.replace('search','')
    query=query.replace('google','')
    query=query.replace('on','')
    query=query.replace(' ','')
    speak("Opening Google",engine)
    if query=='':
        webbrowser.open("https://www.google.com/")
    else:
        q=search(query,num=1,stop=1)
        for res in q:
            webbrowser.open(res)
    time.sleep(5)

def search_google(query,engine):
    speak("finding on google",engine)
    q=search(query,num=1,stop=1)
    for res in q:
        webbrowser.open(res)
    time.sleep(5)

def find_meaning(query,engine):
    query=query.replace('what','')
    query=query.replace('is','')
    query=query.replace('the','')
    query=query.replace('meaning','')
    query=query.replace('find','')
    query=query.replace('of','')
    query=query.replace('tell me','')
    query=query.replace('search','')
    query=query.replace('for','')
    query=query.replace('','')
    dictionary=PyDictionary()
    try:
        mean=dictionary.meaning(query)['Noun'][0]
        speak("The meaning of the word"+query+'is',engine)
        speak(mean,engine)
    except Exception:
        speak("Unable to find the meaning of the given word",engine)

def open_webpage(query,engine):
    speak("opening"+query,engine)
    webbrowser.open('https://'+query+'.com/')
    time.sleep(5)

def get_temperature(query,engine):
    query=query.replace('what','')
    query=query.replace('is','')
    query=query.replace('the','')
    query=query.replace('temperature','')
    query=query.replace('of','')
    query=query.replace('weather','')
    query=query.replace('condition','')
    query=query.replace('in','')
    query=query.replace('climate','')
    query=query.replace('climatic','')
    query=query.replace('condition','')
    query=query.replace(" ",'')
    link='https://api.openweathermap.org/data/2.5/weather?q={}&appid=5591a568869751699e2473e756d21655'.format(query)
    url=requests.get(link)
    try:
        data=url.json()
        speak("Temperature of"+query+'is'+str(round(data['main']['temp']-273.15,2)),engine)
        speak("Humidity in"+query+'is'+str(data['main']['humidity']),engine)
        speak("wind speed in"+query+'is'+str(data['wind']['speed']),engine)
    except Exception:
        speak("Unable to locate the given city name",engine)

def get_score(query,engine):
    try:
        match_data=requests.get("https://cricapi.com/api/cricketScore?unique_id=918033&apikey=JABI4051uYhg9z3EI4e7k9UKcT83").json()
        speak(match_data['stat'],engine)
    except Exception:
        speak("Unable to connect to Server",engine)
