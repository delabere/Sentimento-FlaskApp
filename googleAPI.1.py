#  Google News API Key = fc58cf1054084810a4321540d58de7f1

#rugby request, q=rugby from=2019-10-25 to 2019-11-03 sortby=popularity

#APIKEY = fc58cf1054084810a4321540d58de7f1

# English  -change this to UK???-United States  -change this to sports news?-General news

# https://newsapi.org/docs/endpoints/everything documentation



from config import APIKEY
import requests

url = (f'https://newsapi.org/v2/everything?q=england rugby or rugby&from=2019-10-25&to=2019-11-03&language=en&apiKey={APIKEY}&pagesize=100&page=1')

response = requests.get(url)

with open('news.json', 'w+') as f:
	f.write(response.text)


# #Meta Data for A&B testing
#
# print("Query Status:", response.json()['status'])
# print("total number of results:", response.json()['totalResults'])
#
# #Formatted to make readable in Powershell
#
# for index, DataChunks in enumerate(response.json()['articles']):
#     print(str(index) + "\t ", "**", DataChunks['title'].upper(), "**")
#     print("\t\t ", DataChunks['description'])
