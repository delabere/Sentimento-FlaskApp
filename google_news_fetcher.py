# just something to help you get started mate...

# import the parse function from the newly created google_news_parse module I created
from google_news_parse import parse
import pandas as pd

# from here its just an adaptation of your script:
from config import APIKEY
import requests


parsed_data = pd.DataFrame()

# somehow we need to be able to produce this manually just by specifying the date range (this is the format the API...
# ...wants for datetimes)
time_intervals = ['2019-09-06T00:00:00', '2019-09-06T12:00:00', '2019-10-06T00:00:00', '2019-10-06T12:00:00',
                  '2019-11-06T00:00:00', '2019-11-06T12:00:00']

# put the request somewhere in this loop using the start and end times in the request
for index, _ in enumerate(time_intervals):
    try:
        start = time_intervals[index]
        end = time_intervals[index + 1]
        print(start, end)
    except:
        pass

    # make your request here and pass it into the parse function we imported above
    request_data = parse(# request response has to go in here
    )

    # then concat the dataframes you get out into the one above.
    pd.concat(parsed_data, request_data)


# see how we can make the requests a little more readable using the params argument of the requests.get() method
url = 'https://newsapi.org/v2/everything'
response = requests.get(url, params={
                                'apiKey': APIKEY,
                                'q': 'england rugby or rugby',
                                'pagesize': 100,
                                'from': '2019-10-25',
                                'to': '2019-11-03',
                            })

print(response.json())

