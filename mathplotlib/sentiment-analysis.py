from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 
from textblob import TextBlob
import re
from textblob.sentiments import NaiveBayesAnalyzer



with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    location_counter = Counter()
    
    for row in csv_reader:
        location_counter.update({row['content']})
        
locations = []
tally = []

for location in location_counter.most_common(5):
    locations.append(location[0])
    blob = TextBlob(location[0], analyzer=NaiveBayesAnalyzer())
    tally.append(blob.sentiment.classification)

print(locations)
print(tally)

# w = 3
# nitems = len(tally)
# x_axis = np.arange(0, nitems*w, w)    # set up a array of x-coordinates

# fig, ax = plt.subplots(1)
# ax.barh(x_axis, tally)
# ax.set_title('hat countries were tweeters from?')
# ax.set_xlabel('locations')
# ax.set_ylabel('number of users')
# ax.set_yticks(x_axis);
# ax.set_yticklabels(locations);
# plt.show()

