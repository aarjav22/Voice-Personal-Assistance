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

# Import the beautifulsoup
# and request libraries of python.
import requests
import bs4

# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them
text= "geeksforgeeks"
url = 'https://google.com/search?q=' + text

# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get( url )

# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text,
                         "html.parser")
print(soup) 
