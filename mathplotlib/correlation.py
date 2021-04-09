###### this article was used when coding this file: https://machinelearningmastery.com/how-to-calculate-nonparametric-rank-correlation-in-python/ ##### 

from numpy.random import rand
from numpy.random import seed
from scipy.stats import spearmanr
from matplotlib import pyplot as plt
import csv
from collections import Counter 


with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    verified_followers = []
    verified_retweets = []
    
    not_verified_followers = []
    not_verified_retweets = []


    for row in csv_reader:
            if row['user_verified'] == 'true':
                verified_followers.append(int(row['user_follower_count']))
                verified_retweets.append(int(row['retweet_count']))
            elif row['user_verified'] == 'false':
                not_verified_followers.append(int(row['user_follower_count']))
                not_verified_retweets.append(int(row['retweet_count']))
            else:
                pass

# draw the scatter graph
plt.scatter(verified_followers, verified_retweets)
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)
plt.xlabel('Followers count')
plt.ylabel('Retweets count')
plt.title('Verified users')
plt.show()


# calculate spearman's correlation
coef, p = spearmanr(verified_followers, verified_retweets)
print('Spearmans correlation coefficient of verified accounts: %.9f' % coef)
# interpret the significance
alpha = 0.05
if p > alpha:
	print('Samples are uncorrelated (fail to reject H0) p=%.9f' % p)
else:
	print('Samples are correlated (reject H0) p=%.9f' % p)

# draw the scatter graph
plt.scatter(not_verified_followers, not_verified_retweets)
plt.xlabel('Followers count')
plt.ylabel('Retweets count')
plt.title('Non verified users')
plt.show()

 # calculate spearman's correlation
coef, p = spearmanr(not_verified_followers, not_verified_retweets)
print('Spearmans correlation coefficient of not verified accounts: %.9f' % coef)
# interpret the significance
alpha = 0.05
if p > alpha:
	print('Samples are uncorrelated (fail to reject H0) p=%.9f' % p)
else:
	print('Samples are correlated (reject H0) p=%.9f' % p)