from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 
import ast
import pandas as pd
from textblob import TextBlob
import re
from textblob.sentiments import NaiveBayesAnalyzer
from iso639 import languages

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) #removing hyperlinks and special charaters


def analyse_tweet(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0: # positive
        return "positive"
    elif analysis.sentiment.polarity == 0: # neutral / we don't know
        pass
    else: # negative
        return "negative"
    
with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    sentiments_english = []
    num_english = []
    
    sentiments_farsi= []
    num_farsi = []

    for row in csv_reader:
        if row['language'] == '"en"':
            sentiments_english.append(analyse_tweet(row['content'])) 
            num_english.append(TextBlob(row['content']).sentiment.polarity)
        if row['language'] == '"fa"':
            sentiments_farsi.append(analyse_tweet(row['content'])) 
            num_farsi.append(TextBlob(row['content']).sentiment.polarity)
        else:
            pass

data_english = {'Sentiment':sentiments_english,'Value':num_english}
data_english_pd = pd.DataFrame(data_english)

data_english_pd.boxplot(by='Sentiment', column='Value')
plt.xlabel('Sentiment of tweets')
plt.ylabel('Polarity value')
plt.title('Sentiment analysis on English tweets')
plt.show()

data_farsi = {'Sentiment':sentiments_farsi,'Value':num_farsi}
data_farsi_pd = pd.DataFrame(data_farsi)

data_farsi_pd.boxplot(by='Sentiment', column='Value')
plt.xlabel('Sentiment of tweets')
plt.ylabel('Polarity value')
plt.title('Sentiment analysis on Farsi tweets')
plt.show()
