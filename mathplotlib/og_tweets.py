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
    
    count = 0
    
    for row in csv_reader:
        if not str({row['content']}).startswith("{\'\"RT "):
            user_id_counter.update({row['user_id']})
            if row['user_id'] in followers:
                followers[row['user_id']] = [row['user_follower_count'], row['user_verified']]
            else:
                followers[row['user_id']] = [0,False]
    user = []
    tally = []

    follower_num = []
    user = []
    verified = []

    i = 1

    data = []
    for tweet in user_id_counter.most_common(10):
        temp = []
        temp.append("user {}".format(i))
        temp.append(int(followers[tweet[0]][0]))
        temp.append(followers[tweet[0]][1])
        data.append(temp)
        i+=1
                
             
    fig, ax = plt.subplots(1,1)
    column_labels=["user", "follower count", "verified"]
    ax.axis('tight')
    ax.axis('off')
    ax.set_title("Top 10 users who sent the most orginial tweets")
    the_table = ax.table(cellText=data,colLabels=column_labels,colColours =["pink"] * 3,loc="center")
    
    the_table[(1, 0)].set_facecolor("green")
    the_table[(1, 1)].set_facecolor("green")
    the_table[(1, 2)].set_facecolor("green")
    
    the_table[(4, 0)].set_facecolor("green")
    the_table[(4, 1)].set_facecolor("green")
    the_table[(4, 2)].set_facecolor("green")

    plt.show()
