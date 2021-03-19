"""url='https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/206bbbf3-fd4a-4056-8d60-08d71df421d2'
key='nFPkrGzuJRK7OR-KxjQOEIqTxZfG1eIqc1Tf4-7A-lYx'
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import simpleaudio as sa

authenticator = IAMAuthenticator(key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

test="Hello every one!."

text_to_speech.set_service_url(url)

'''
voices = text_to_speech.list_voices().get_result()
print(json.dumps(voices, indent=3))
'''

with open('temp.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            test,
            voice='en-US_HenryV3Voice',
            accept='audio/wav'
        ).get_result().content)


wave_obj = sa.WaveObject.from_wave_file("temp.wav")
play_obj = wave_obj.play()
play_obj.wait_done()"""

"""import requests
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
    print("vcxvx")
    #playsound("./sound/news.wav")
article = open_bbc_page["articles"]
print(article[0]['title'])
print(article[1])
"""

import valib as va
import action as a
import time
import logging

logger = logging.getLogger('voice assistant')


def process_text(text, pa):

    """
    asking who are you?
    """
    if "who are you" in text:
        va.audio_playback("i am a i voice assistant system")

    """
    asking about weather information.
    """
    if "weather" in text:
        va.audio_playback("which city")
        time.sleep(0.5)
        file_name = pa.process(3)
        city = pa.voice_command_processor(file_name)
        logger.info("process_text : City :: " + city)
        try:
            humidity, temp, phrase = a.weatherReport(city)
            va.audio_playback(
                "currently in " + city + " temperature is " + str(temp) + " degree celsius, " + "humidity is " + str(
                    humidity) + " percent and sky is " + phrase)
            logger.info("currently in " + city + " temperature is " + str(temp) + "degree celsius, " + "humidity is " + str(
                humidity) + " percent and sky is " + phrase)
        except KeyError as e:
            va.audio_playback("sorry, i couldn't get the location")


    """
    asking for search somthing like:
    what is raspberry pi
    who is isac newton etc.
    """
    if "search" in text or "Search" in text:
        va.audio_playback("tell me what to search")
        time.sleep(0.5)
        file_name = pa.process(5)
        search_data = pa.voice_command_processor(file_name)
        try:
            result = a.google_search(search_data)
            if result:
                va.audio_playback(result)
            else:
                va.audio_playback("sorry, i couldn't find any result for " + search_data)
        except KeyError as e:
            va.audio_playback("sorry, i couldn't find any result for " + search_data)
            pass


    """
    asking aboout current time.
    """
    if "time" in text or "Time" in text:
        current_time = a.current_datetime("time")
        va.audio_playback("right now it is " + current_time)

    """
    asking about today's date.
    """
    if "date" in text or "Date" in text:
        date = a.current_datetime("date")
        va.audio_playback("today it is " + date)


    """
    asking for rebooting the voice assistant system.
    """
    if "reboot" in text or "Reboot" in text:
        va.audio_playback("ok.. rebooting the server")
        a.reboot_server()

    return "done"
