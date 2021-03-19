from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 
import ast
from langdetect import detect


##### https://github.com/vprusso/youtube_tutorials/tree/master/twitter_python #####
def get_hashtag_lang(list_of_hastags):
    temp = ast.literal_eval(list_of_hastags) 
    hashtags = []
    for hashtag in temp:
        hashtags.append(detect(hashtag['text']))
    return hashtags
    

with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    hashtag_counter = Counter()
    
    for row in csv_reader:
        hashtag_counter.update(get_hashtag_lang(row['hashtags']))
        
# hashtags = []
# tally = []

print(hashtag_counter.most_common(20))

# for hashtag in hashtag_counter.most_common(20):
#     print(hashtag)
#     hashtags.append(hashtag[0])
#     tally.append(hashtag[1])
# print(hashtags)


# plt.bar(hashtags, tally)
# plt.xlabel('Hashtags')
# plt.ylabel('times')
# plt.title('How many times has each hashtag been mentioned?')
# plt.xticks(rotation=90)
# plt.show()

