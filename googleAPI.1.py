#  Google News API Key = fc58cf1054084810a4321540d58de7f1

#rugby request, q=rugby from=2019-10-25 to 2019-11-03 sortby=popularity

#APIKEY = fc58cf1054084810a4321540d58de7f1

# English  -change this to UK???-United States  -change this to sports news?-General news

# https://newsapi.org/docs/endpoints/everything documentation

import requests
url = ('https://newsapi.org/v2/everything?q=england rugby or rugby&from=2019-10-25&to=2019-11-03&language=en&apiKey=fc58cf1054084810a4321540d58de7f1')

response = requests.get(url)

#Meta Data for A&B testing

print("Query Status:", response.json()['status'])
print("total number of results:", response.json()['totalResults'])

#Formatted to make readable in Powershell

for DataChunks in response.json()['articles']:
    print("\t ", "**", DataChunks['title'].upper(), "**")
    print("\t\t ", DataChunks['description'])
