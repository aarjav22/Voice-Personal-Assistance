import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
from googlesearch import search
from PyDictionary import PyDictionary
import os
from youtubesearchpython import VideosSearch
from youtubesearchpython import PlaylistsSearch
import requests
import json
import vlc
import pafy
import re
from pytube import Playlist
import random

def engine_init():
    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    return engine

def speak(text,engine):
    engine.say(text)
    engine.runAndWait()

def welcome(engine):
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        player = vlc.MediaPlayer("./sound/goodmorning.mp3")
        player.play()
    elif hour>=12 and hour<18:
        player = vlc.MediaPlayer("./sound/goodafternoon.mp3")
        player.play()
    else:
        player = vlc.MediaPlayer("./sound/goodevening.mp3")
        player.play()

    player = vlc.MediaPlayer("./sound/init.mp3")
    player.play()

def record(engine):
	r=sr.Recognizer()
	mic=sr.Microphone(device_index = 1)

	with mic as source:
		print("listeninig....")
		r.adjust_for_ambient_noise(source,duration=1)
		audio=r.listen(source)

	try:
		print("recognizing....")
		query=r.recognize_google(audio)

	except Exception:
        player = vlc.MediaPlayer("./sound/recorgnising_error.mp3")
        player.play()
		return None
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
        player = vlc.MediaPlayer("./sound/wikipedia.mp3")
        player.play()

def play_song(query,engine):
    query=query.replace('any','')
    query=query.replace('some','')
    query=query.replace('random','')
    query=query.replace('play','')
    if 'songs' in query or 'song' in query or 'music' in query or 'musics' in query:
        playlistsSearch = PlaylistsSearch(query, limit = 2)
        url=str(playlistsSearch.result()['result'][0]['link'])
        playlist = Playlist(url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        url=playlist.video_urls[random.randint(0,len(playlist.video_urls)-1)]
        video=pafy.new(url)
        audiostreams=video.audiostreams
        song=audiostreams[0]
        song.download("temp."+song.extension)
        player = vlc.MediaPlayer("./sound/music.mp3")
        player.play()
        player = vlc.MediaPlayer("./temp."+song.extension)
        player.play()
        return True,player,song
    else:
        videosSearch = VideosSearch(query, limit=2)
        url=str(videosSearch.result()['result'][0]['link'])
        #url=f"https://www.youtube.com/watch?v="+result
        video=pafy.new(url)
        audiostreams=video.audiostreams
        song=audiostreams[0]
        song.download("temp."+song.extension)
        player = vlc.MediaPlayer("./sound/music.mp3")
        player.play()
        player = vlc.MediaPlayer("./temp."+song.extension)
        player.play()
        return True,player,song

def search_google(query,engine):
    player = vlc.MediaPlayer("./sound/google.mp3")
    player.play()
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
        player = vlc.MediaPlayer("./sound/meaning.mp3")
        player.play()

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
    query=query.replace('wear','')
    query=query.replace(" ",'')
    link='https://api.openweathermap.org/data/2.5/weather?q={}&appid=5591a568869751699e2473e756d21655'.format(query)
    url=requests.get(link)
    try:
        data=url.json()
        speak("Temperature of"+query+'is'+str(round(data['main']['temp']-273.15,2)),engine)
        speak("Humidity in"+query+'is'+str(data['main']['humidity']),engine)
        speak("wind speed in"+query+'is'+str(data['wind']['speed']),engine)
    except Exception:
        player = vlc.MediaPlayer("./music/weather.mp3")
        player.play()

def get_score(query,engine):
    try:
        match_data=requests.get("https://cricapi.com/api/cricketScore?unique_id=918033&apikey=JABI4051uYhg9z3EI4e7k9UKcT83").json()
        speak(match_data['stat'],engine)
    except Exception:
        player = vlc.MediaPlayer("./music/score.mp3")
        player.play()


def get_news(engine):
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "32de7139615644cd8c6545d5ef463105"
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
    player = vlc.MediaPlayer("./music/news.mp3")
    player.play()
    for i in range(3):
        speak(results[i],engine)
        time.sleep(0.8)
