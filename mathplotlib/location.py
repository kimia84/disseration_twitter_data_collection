from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 


with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    location_counter = Counter()
    
    for row in csv_reader:
        location_counter.update({row['location']})
        
locations = []
tally = []


for location in location_counter.most_common(20):
    locations.append(location[0])
    tally.append(location[1])

locations.pop(0)
tally.pop(0)

w = 3
nitems = len(tally)
x_axis = np.arange(0, nitems*w, w)    # set up a array of x-coordinates

fig, ax = plt.subplots(1)
ax.barh(x_axis, tally)
ax.set_title('hat countries were tweeters from?')
ax.set_xlabel('locations')
ax.set_ylabel('number of users')
ax.set_yticks(x_axis);
ax.set_yticklabels(locations);
plt.show()

