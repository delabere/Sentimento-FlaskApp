# time interval module
from datetime import datetime, timedelta

parsed_data = pd.DataFrame()

# Time interval generation

#datetime(year, month, day)

start_date= datetime(2019,10,25)
end_date= datetime(2019,11,5)
diff= (end_date-start_date).days+1

time_intervals = []

for d in range(diff):
    time_intervals.append(str(start_date+timedelta(d)))
    #timedelta doesn't take hours - need to think about repitition a day

# put the request somewhere in this loop using the start and end times in the request
for index, _ in enumerate(time_intervals):
    try:
        start = time_intervals[index]
        end = time_intervals[index + 1]
        print(start, end)
