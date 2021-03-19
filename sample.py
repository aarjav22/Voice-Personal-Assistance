from friday_functions import *

engine=engine_init()
welcome()
music_flag=False
player=None
song=None

while True:
    query=record(engine).lower()
    if query=="not recorgnized":
        print("aarjav")
        continue;
    print(query)
    if 'prabhu' in query or 'prawhu' in query or 'parabhu' in query or 'pabhu' in query:
        if music_flag:
            player.stop()
            os.remove('./temp.'+song.extension)
            music_flag=False
            player=None
            song=None
        playsound("./sound/wake_sound.wav")
        query=record(engine).lower()
        print(query)
        if 'prabhu' in query or 'prawhu' in query or 'parabhu' in query or 'pabhu' in query:
            if 'bye' not in query and 'goodbye' not in query and 'stop' not in query:
                playsound("./sound/greeting.wav")
            else:
                playsound("./sound/thank_you.wav")
                break

        elif 'bye' in query or 'stop' in query or 'end' in query or 'goodbye' in query:
            playsound("./sound/thank_you.wav")
            break

        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            text_to_speech("Current time is "+str(time),engine)

        elif 'date' in query:
            date=datetime.date.today()
            text_to_speech("Today's date is "+str(date),engine)

        elif 'day' in query:
            day=datetime.datetime.now().strftime("%A")
            text_to_speech("Today's day is "+str(day),engine)

        elif 'wiki' in query or 'wikipedia' in query or "who is" in query or ('what' in query and 'meaning' not in query and 'temperature' not in query and 'news' not in query and 'affairs' not in query and 'score' not in query):
            search_wikipedia(query,engine)

        elif 'song' in query or 'play' in query or 'music' in query or 'songs' in query or 'musics' in query:
            music_flag,player,song=play_song(query,engine)

        elif 'google' in query or ('search' in query and 'meaning' not in query):
            search_google(query,engine)

        elif 'meaning' in query:
            find_meaning(query,engine)

        elif 'temperature' in query or 'weather' in query or 'climate' in query or 'climatic' in query:
            get_temperature(query,engine)

        elif "cricket" in query or "score" in query or "match" in query:
            get_score(query,engine)

        elif "news" in query or 'affairs' in query or 'headlines' in query or 'affair' in queue:
            get_news(engine)

    else:
        playsound("./sound/error.wav")
