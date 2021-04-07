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

def set_align_for_column(table, col, align="left"):
    cells = [key for key in table._cells if key[1] == col]
    for cell in cells:
        table._cells[cell]._loc = align
    

with open('twitterData_public_tweets.csv') as file:
    csv_reader =  csv.DictReader(file)
    
    hashtag_na = Counter()
    hashtag_us = Counter()
    hashtag_blank = Counter()
    hashtag_ca = Counter()
    hashtag_ge = Counter()
    hashtag_ir = Counter()
    hashtag_uk = Counter()
    hashtag_pa = Counter()
    hashtag_nz = Counter()
    hashtag_go = Counter()
    hashtag_li = Counter()
    
    for row in csv_reader:
        if row['location'] == '"N/A"':
            hashtag_na.update(get_hashtags(row['hashtags']))
        elif row['location'] == '"United States"':
            hashtag_us.update(get_hashtags(row['hashtags']))
        elif row['location'] == '""':
            hashtag_blank.update(get_hashtags(row['hashtags']))
        elif row['location'] == '"Canada"':
            hashtag_ca.update(get_hashtags(row['hashtags']))
        elif row['location'] == '"Germany"':
            hashtag_ge.update(get_hashtags(row['hashtags']))
        elif row['location'] ==  '"Islamic Republic of Iran"':
            hashtag_ir.update(get_hashtags(row['hashtags']))
        elif row['location'] ==  '"United Kingdom"':
            hashtag_uk.update(get_hashtags(row['hashtags']))
        elif row['location'] ==  '"Pakistan"':
            hashtag_pa.update(get_hashtags(row['hashtags']))
        elif row['location'] ==  '"New Zealand"':
            hashtag_nz.update(get_hashtags(row['hashtags']))
        elif row['location'] ==  '"Georgia"':
            hashtag_go.update(get_hashtags(row['hashtags']))
        elif row['location'] ==  '"Liechtenstein"':
            hashtag_li.update(get_hashtags(row['hashtags']))
        else:
            pass
        
data = []

temp = []
for hashtag in hashtag_na.most_common(5):
        temp.append(hashtag[0])
data.append(["N/A",temp])

temp = []
for hashtag in hashtag_us.most_common(5):
        temp.append(hashtag[0])
data.append(["United States",temp])

temp = []
for hashtag in hashtag_blank.most_common(5):
        temp.append(hashtag[0])
data.append(["Blank",temp])

temp = []
for hashtag in hashtag_ca.most_common(5):
        temp.append(hashtag[0])
data.append(["Canada",temp])

temp = []
for hashtag in hashtag_ge.most_common(5):
        temp.append(hashtag[0])
data.append(["Germany",temp])

temp = []
for hashtag in hashtag_ir.most_common(5):
        temp.append(hashtag[0])
data.append(["Iran",temp])



temp = []
for hashtag in hashtag_uk.most_common(5):
        temp.append(hashtag[0])
data.append(["United Kingdom",temp])

temp = []
for hashtag in hashtag_pa.most_common(5):
        temp.append(hashtag[0])
data.append(["Pakistan",temp])

temp = []
for hashtag in hashtag_nz.most_common(5):
        temp.append(hashtag[0])
data.append(["New Zealand",temp])

temp = []
for hashtag in hashtag_go.most_common(5):
        temp.append(hashtag[0])
data.append(["Georgia",temp])

temp = []
for hashtag in hashtag_li.most_common(5):
        temp.append(hashtag[0])
data.append(["Liechtenstein",temp])

fig, ax = plt.subplots(1,1)
column_labels=["Location", "Top 5 hashtags"]
ax.axis('off')
ax.set_title("Top 5 hashtags per locations")
the_table = ax.table(cellText=data,colLabels=column_labels,colColours =["plum"] * 2,loc="center")
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.auto_set_column_width(col=2)
plt.show()
