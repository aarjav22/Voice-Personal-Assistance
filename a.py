import requests
def NewsFromBBC():
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
    for i in range(len(results)):
        print(i + 1, results[i])
if __name__ == '__main__':
    NewsFromBBC()


#api=32de7139615644cd8c6545d5ef463105
