from google_news_parse import parse
import pandas as pd
from config import APIKEY
import requests
from datetime import datetime, timedelta

parsed_data = pd.DataFrame()

start_date= datetime(2019,10,25)
end_date= datetime(2019,11,5)
diff= (end_date-start_date).days+1

time_intervals = []

for d in range(diff):
    time_intervals.append(str(start_date+timedelta(d)))

url = 'https://newsapi.org/v2/everything'

for index, _ in enumerate(time_intervals):
    try:
        start = time_intervals[index]
        end = time_intervals[index + 1]
        response = requests.get(url, params={
                                'apiKey': APIKEY,
                                'q': 'england rugby or rugby',
                                'pagesize': 100,
                                'from': start,
                                'to': end,
                            })
        request_data = parse(response)
        parsed_data = parsed_data.append(request_data)
    except:
        print("We did it!")
        break

parsed_data.to_csv("data/rugby_data.csv", index=False)
