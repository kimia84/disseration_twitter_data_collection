import twitter
import os
from dotenv import load_dotenv
import psycopg2
from pathlib import Path 
from datetime import datetime 

# retrieve sensetive env data
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#### connect to database to store our data - https://www.psycopg.org/docs/install.html#quick-install ####
# Connect to your postgres DB
conn = psycopg2.connect("host=localhost dbname=twitterData user=kimiapirouzkia")

# Open a cursor to perform database operations
cur = conn.cursor()


#times of the protest
start_date = "Fri Nov 15 00:00:00 +0000 2019"
end_date = "Tue Dec 16 00:00:00 +0000 2020"

def extract_hashtags_from_tweets(tweet):
    extra_hashtags = []
    words = tweet.split()
    for word in words:
        letters = list(word)
        if letters[0] == '#':
            extra_hashtags.append(word)
    return extra_hashtags

#### https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/ ####
def extract_initial_hashtags_from_text_file():
    hashtags = []
    f = open("hashtags.txt", "r")
    for line in f:
        hashtags.append(line.strip())
 
    f.close()
    return hashtags

def get_country(place):
    if not place:
        return "N/A"
    return place["country"]

def main():
    consumer_key=os.getenv('CONSUMER_KEY')
    consumer_secret=os.getenv('CONSUMER_SECRET')
    access_token_key=os.getenv('ACCESS_TOKEN_KEY')
    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')

    api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

    hashtags = extract_initial_hashtags_from_text_file()
    data = {}
    extra_hashtags = {}

    time = '2020-12-16'

    for hashtag in hashtags:
        tweets = api.GetSearch(term=hashtag, count=7000, since='2019-11-15', until=time)
        for tweet in tweets:
            data[tweet.created_at] = (tweet.text, tweet.geo)
            temp = extract_hashtags_from_tweets(tweet.text)
            for t in temp:
                if t not in extra_hashtags:
                    extra_hashtags[t] = 1
                else:
                    extra_hashtags[t] += 1
            # if tweet.create_at != start_date:
            cur.execute("INSERT INTO tweets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (get_country(tweet.place), tweet.text, '#'.join(temp), tweet.id,  tweet.user.id, tweet.lang, tweet.user.followers_count, tweet.retweet_count , tweet.user.verified, tweet.created_at))
            conn.commit()
            # new_datetime = datetime.strftime(datetime.strptime(tweet.created_at ,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d')
            # time = 
    print(len(tweets))

if __name__ == "__main__":
    main()