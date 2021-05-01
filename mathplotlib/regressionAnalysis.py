import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import csv
from collections import Counter 
import ast
from langdetect import detect
from textblob import TextBlob
import re
from textblob.sentiments import NaiveBayesAnalyzer

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) #removing hyperlinks and special charaters

def analyse_tweet(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity 

with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    follower_count = {}
    
    for row in csv_reader:
        follower_count[int(row['user_follower_count'])] = analyse_tweet(row['content'])

       
test = {key:val for key, val in follower_count.items() if val != 0}


y = list(test.keys())
x = list(test.values())


slope, intercept, r, p, std_err = stats.linregress(x, y)
print("slope: {}".format(slope))
print("intersect: {}".format(intercept))
print("r: {}".format(r))
print("p: {}".format(p))
print("std_err: {}".format(std_err))

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))


plt.scatter(x, y, color = 'green')
# plt.xlim(0, 400)
plt.ylim(0, 30000)
plt.plot(x, mymodel, 'red')
plt.xlabel('polarity values of tweets')
plt.ylabel('number of followers')
plt.title('correlation between follower count and polarity of each tweet')
plt.show()
