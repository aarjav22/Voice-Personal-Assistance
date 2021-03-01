import requests
import bs4
text= "dhoni"
url = 'https://google.com/search?q=' + text
request_result=requests.get( url )
#soup = bs4.BeautifulSoup(request_result.text,
#                         "html.parser")
print(request_result.text)
