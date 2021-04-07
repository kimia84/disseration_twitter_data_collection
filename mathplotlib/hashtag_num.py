from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 
import ast

def get_hashtags(list_of_hastags):
    temp = ast.literal_eval(list_of_hastags) 
    hashtags = []
    for hashtag in temp:
        hashtags.append(hashtag['text'])
    return hashtags
    

with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    hashtag_counter = Counter()
    
    for row in csv_reader:
        hashtag_counter.update(get_hashtags(row['hashtags']))
        
hashtags = []
tally = []


for hashtag in hashtag_counter.most_common(20):
    hashtags.append(hashtag[0])
    tally.append(hashtag[1])


plt.bar(hashtags, tally, color="grey")
plt.xlabel('Hashtags')
plt.ylabel('times')
plt.title('How many times has each hashtag been mentioned?')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

