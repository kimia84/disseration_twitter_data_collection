from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter 
import ast

with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    user_id_counter = Counter()
    followers = {}
    
    for row in csv_reader:
        user_id_counter.update({row['user_id']})
        followers[row['user_id']] = [row['user_follower_count'], row['user_verified']]
        
user = []
tally = []

follower_num = []
verified = Counter()

i = 1

for tweet in user_id_counter.most_common(10):
    user.append("user {}".format(i))
    tally.append(tweet[1])
    
    follower_num.append(followers[tweet[0]][0])
    verified.update({followers[tweet[0]][1]})
    i+=1

verified_name = []
verified_tally = []
for tweet in verified.most_common(3):
    verified_name.append(tweet[0])
    verified_tally.append(tweet[1])


plt.bar(user, tally)
plt.xlabel('Top users')
plt.ylabel('number of tweets')
plt.title('Who sent the most tweets out?')
# plt.xticks()
plt.show()

plt.bar(follower_num, user)
plt.xlabel('Top users')
plt.ylabel('number of followers')
plt.title('Level of influence?')
plt.show()


plt.bar(verified_name, verified_tally)
plt.xlabel('Top users')
plt.ylabel('verified?')
plt.title('Level of influence?')
plt.show()
