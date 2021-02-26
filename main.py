from friday_functions import *

engine=engine_init()
welcome(engine)

music_dir='F:\\bhajan'

while True:
    query=record(engine).lower()

    if 'friday' in query:
        if 'bye' not in query and 'goodbye' not in query and 'stop' not in query:
            speak("How may I help you sir!",engine)
        else:
            speak("Thank You for your time sir",engine)
            break

    elif 'bye' in query or 'stop' in query or 'end' in query or 'goodbye' in query:
        speak("Thank You for your time sir",engine)
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

    elif 'wiki' in query or 'wikipedia' in query or "who is" in query or ('what is' in query and 'meaning' not in query):
        search_wikipedia(query,engine)

    elif 'youtube' in query or 'play' in query:
        open_youtube(query,engine)

    elif 'google' in query or ('search' in query and 'meaning' not in query):
        open_google(query,engine)

    elif 'meaning' in query:
        find_meaning(query,engine)

    elif 'stackoverflow' in query or 'stack overflow' in query or 'stack over flow' in query:
        open_webpage('stackoverflow',engine)

    elif 'github' in query or 'git hub' in query:
        open_webpage('github',engine)

    elif 'play song' in query or 'music' in query or 'play music' in query:
        play_music(music_dir,engine)

    #elif 'open' in query:
    elif 'how to' :
        search_google(query,engine)
