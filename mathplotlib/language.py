from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
from iso639 import languages

with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    language_counter = Counter()
    
    for row in csv_reader:
        language_counter.update({row['language']})
        
languages_list = []
tally = []


for language in language_counter.most_common(100):
    languages_list.append(languages.get(alpha2=language[0]).name)
    tally.append(language[1])

plt.bar(languages_list, tally)
plt.xlabel('languages')
plt.ylabel('number of tweets')
plt.title('The language of tweets')
plt.xticks(rotation=90)
plt.show()
