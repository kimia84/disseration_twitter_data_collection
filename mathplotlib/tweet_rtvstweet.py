from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 
import ast
import pandas as pd

with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)

    user_id_counter = Counter()
    followers = {}
    
    for row in csv_reader:
        user_id_counter.update({row['user_id']})
        if row['user_id'] in followers:
            if str({row['content']}).startswith("{\'\"RT "):
                followers[row['user_id']][1] += 1
            else:
                followers[row['user_id']][0] += 1
        else:
            if str({row['content']}).startswith("{\'\"RT "):
                followers[row['user_id']] = [0, 1]
            else:
                followers[row['user_id']] = [1, 0] # [tweet_count, retweet_count]
            
    x = []
    tweet_count = []
    rt_count = []  
    
    i = 1  
     
    for tweet in user_id_counter.most_common(20):
        tweet_count.append(followers[tweet[0]][0])
        rt_count.append(followers[tweet[0]][1])
        x.append("user {}".format(i))
        
        i+=1
 


df = pd.DataFrame(np.c_[tweet_count,rt_count], index=x, columns=["Original tweets","Retweets"])
df.plot.bar()

plt.show()

