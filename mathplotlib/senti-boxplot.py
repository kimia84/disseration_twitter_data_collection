from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 
import ast
import pandas as pd
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
    
    sentiments = []
    num = []

    for row in csv_reader:
        sentiments.append(analyse_tweet(row['content'])) 
        num.append(TextBlob(row['content']).sentiment.polarity)
        

data = {'Sentiment':sentiments,'Value':num}
data_pd = pd.DataFrame(data)

data_pd.boxplot(by='Sentiment', column='Value')
plt.xlabel('Sentiment of tweets')
plt.ylabel('Polarity value')
plt.show()
