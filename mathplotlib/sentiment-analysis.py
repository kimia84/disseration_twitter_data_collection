from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 
from textblob import TextBlob
import re
from textblob.sentiments import NaiveBayesAnalyzer

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) #removing hyperlinks and special charaters

def analyse_tweet(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0: # positive
        return "positive"
    elif analysis.sentiment.polarity == 0: # neutral / we don't know
        return "neutral"
    else: # negative
        return "negative"
    
with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    sentiment_counter = Counter()

    for row in csv_reader:
        sentiment_counter.update({analyse_tweet(row['content'])})
        
sentiments = []
tally = []

for sentiment in sentiment_counter.most_common(5):
    sentiments.append(sentiment[0])
    tally.append(sentiment[1])

w = 3
nitems = len(tally)
x_axis = np.arange(0, nitems*w, w)    # set up a array of x-coordinates

fig, ax = plt.subplots(1)
ax.barh(x_axis, tally)
ax.set_title('What is the sentiment of each tweet?')
ax.set_xlabel('Sentiment')
ax.set_ylabel('number of tweets')
ax.set_yticks(x_axis);
ax.set_yticklabels(sentiments);
plt.show()

