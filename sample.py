from friday_functions import *
from playsound import playsound

engine=engine_init()
welcome(engine)
music_flag=False
player=None
song=None

while True:
    query=record(engine).lower()
    if 'prabhu' in query or 'prawhu' in query or 'parabhu' in query or 'pabhu' in query:
        if music_flag:
            player.stop()
            os.remove('./temp.'+song.extension)
            music_flag=False
            player=None
            song=None
        playsound('./sound/wake_sound.wav')
        query=record(engine).lower()
        if 'prabhu' in query or 'prawhu' in query or 'parabhu' in query or 'pabhu' in query:
            if 'bye' not in query and 'goodbye' not in query and 'stop' not in query:
                speak("How may I help you sir!",engine)
            else:
                speak("Thank You for your time sir",engine)
                break

        elif 'bye' in query or 'stop' in query or 'end' in query or 'goodbye' in query:
            speak("Thank You ",engine)
            break

        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak("Current time is "+str(time),engine)

        elif 'date' in query:
            date=datetime.date.today()
            speak("Todays date is "+str(date),engine)

        elif 'day' in query:
            day=datetime.datetime.now().strftime("%A")
            speak("Today's day is "+str(day),engine)

        elif 'wiki' in query or 'wikipedia' in query or "who is" in query or ('what is' in query and 'meaning' not in query and 'temperature' not in query):
            search_wikipedia(query,engine)

        elif 'song' in query or 'play' in query or 'music' in query:
            music_flag,player,song=play_song(query,engine)

        elif 'google' in query or ('search' in query and 'meaning' not in query):
            open_google(query,engine)

        elif 'meaning' in query:
            find_meaning(query,engine)

        elif 'temperature' in query or 'weather' in query or 'climate' in query or 'climatic' in query:
            get_temperature(query,engine)

        elif "cricket" in query or "score" in query or "match" in query:
            get_score(query,engine)

    else:
        print("not prabhu")
