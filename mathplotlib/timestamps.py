from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 
from datetime import datetime


with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    daily_timestamps = Counter()
    
    for row in csv_reader:
        daily_timestamps.update({str(datetime.strptime(row['created_at'],'"%a %b %d %H:%M:%S %z %Y"').date())})

timestamps = []
tally = []


for timestamp in sorted(daily_timestamps.items()):
    timestamps.append(timestamp[0])
    tally.append(timestamp[1])
    

plt.bar(timestamps, tally)
plt.xlabel('Timestamps')
plt.ylabel('number of tweets')
plt.title('How many tweets were sent out everyday?')
plt.xticks(rotation=90)
plt.show()

