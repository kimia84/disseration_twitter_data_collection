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
    highest_follower = ''
    
    for row in csv_reader:
        user_id_counter.update({row['user_id']})
        followers[row['user_id']] = [row['user_follower_count'], row['user_verified']]
        if int(row['user_follower_count']) > count:
            highest_follower = row['user_id']
            count = int(row['user_follower_count'])
    
user = []
tally = []

follower_num = []
user = []
verified = Counter()

i = 1

data = []
data.append(["Most followed user",count])
for tweet in user_id_counter.most_common(10):
    temp = []
    temp.append("user {}".format(i))
    print(tweet[0])
    temp.append(int(followers[tweet[0]][0]))
    data.append(temp)
    
    follower_num.append(float(followers[tweet[0]][0]))
    user.append(tweet[0])
    verified.update({followers[tweet[0]][1]})
    i+=1

verified_name = []
verified_tally = []

for tweet in verified.most_common(3):
    verified_name.append(tweet[0])
    verified_tally.append(tweet[1])


fig, ax = plt.subplots(1,1)
column_labels=["user", "follower count"]
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=data,colLabels=column_labels,colColours =["yellow"] * 2,loc="center")
the_table[(1, 0)].set_facecolor("#1ac3f5")
the_table[(1, 1)].set_facecolor("#1ac3f5")

plt.show()

# y_pos = np.arange(len(user))


# # Basic plot
# plt.bar(y_pos, follower_num, color='orange')

# plt.title('The follower count of the top ten most tweeted users')
# plt.xticks(y_pos, user, color='black', rotation=45, horizontalalignment='right')
# plt.show()
 
# # remove labels
# plt.tick_params(labelbottom=False)
# plt.show()

# plt.bar(user, tally)
# plt.xlabel('Top users')
# plt.ylabel('number of tweets')
# plt.title('Who sent the most tweets out?')
# # plt.xticks()
# plt.show()

# plt.pie(verified_tally, labels = verified_name, shadow=True)
# plt.title('How many users are verified?')
# plt.show() 
