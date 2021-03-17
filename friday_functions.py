import speech_recognition as sr
#import pyttsx3
import datetime
import wikipedia
#import webbrowser
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
import simpleaudio as sa
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def engine_init():
    url='https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/206bbbf3-fd4a-4056-8d60-08d71df421d2'
    key='nFPkrGzuJRK7OR-KxjQOEIqTxZfG1eIqc1Tf4-7A-lYx'
    authenticator = IAMAuthenticator(key)
    text_to_speech = TextToSpeechV1(
    authenticator=authenticator
    )
    text_to_speech.set_service_url(url)
    return text_to_speech

def text_to_speech(text,engine):
    with open('temp.wav', 'wb') as audio_file:
        audio_file.write(
            engine.synthesize(
                text,
                voice='en-US_MichaelV3Voice',
                accept='audio/wav'
            ).get_result().content)

    playsound("temp.wav")
    os.remove('temp.wav')

"""def speak(text,engine):
    engine.say(text)
    engine.runAndWait()
"""
def playsound(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def welcome():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        playsound("./sound/goodmorning.wav")
    elif hour>=12 and hour<18:
        playsound("./sound/goodafternoon.wav")
    else:
        playsound("./sound/goodevening.wav")

    playsound("./sound/init.wav")

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
         playsound("./sound/recorgnising_error.wav")
         return "Not recorgnized"
	return query

def search_wikipedia(query,engine):
    query=query.replace("wikipedia","")
    query=query.replace("wiki","")
    query=query.replace("who is","")
    query=query.replace("what is","")
    try:
        result=wikipedia.summary(query,sentences=1)
        text_to_speech("according to wikipedia"+result,engine)
    except Exception as e:
        playsound("./sound/wikipedia.wav")

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
        playsound("./sound/music.wav")
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
        playsound("./sound/music.wav")
        player = vlc.MediaPlayer("./temp."+song.extension)
        player.play()
        return True,player,song

def search_google(query,engine):
    playsound("./sound/google.wav")
    q=search(query,num=1,stop=1)
    for res in q:
        #webbrowser.open(res)
        print("aarjav")
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
        text_to_speech("The meaning of the word"+query+'is'+mean,engine)
    except Exception:
        playsound("./sound/meaning.wav")

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
        text_to_speech("Temperature is"+str(round(data['main']['temp']-273.15,2))+'.'+"Humidity is"+str(data['main']['humidity'])+'.'+
        "wind speed is"+str(data['wind']['speed'])+'.',engine)

    except Exception:
        playsound("./sound/weather.wav")

def get_score(query,engine):
    try:
        match_data=requests.get("https://cricapi.com/api/cricketScore?unique_id=918033&apikey=JABI4051uYhg9z3EI4e7k9UKcT83").json()
        text_to_speech(match_data['stat'],engine)
    except Exception:
        playsound("./sound/score.wav")


def get_news(engine):
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "32de7139615644cd8c6545d5ef463105"
    }
    main_url = " https://newsapi.org/v1/articles"
    try:
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
    except Exception:
        playsound("./sound/news.wav")
        return None
    article = open_bbc_page["articles"]
    text_to_speech(article[0]['title'],engine)
