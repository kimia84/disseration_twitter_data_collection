import twitter
import os
from dotenv import load_dotenv
import psycopg2
from pathlib import Path 
import datetime 
import requests
import json
import tweepy

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
    return str(place["country"])

def get_hashtags(entities):
    if not entities:
        return "N/A"
    return str(entities["hashtags"])

def main():
    consumer_key=os.getenv('CONSUMER_KEY')
    consumer_secret=os.getenv('CONSUMER_SECRET')
    access_token_key=os.getenv('ACCESS_TOKEN_KEY')
    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')

    # api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

    authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authentication.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    hashtags = extract_initial_hashtags_from_text_file()
    data = {}
    extra_hashtags = {}

    endpoint = "https://api.twitter.com/2/tweets/search/recent?query=snow&max_results=100"
    headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAA9IKQEAAAAAR7hy7%2BBUghmBGZKEeNiy8CvhqYo%3D2XmeSWFSejMJWp4jSkT5IUE0gcwyJuCwybJ4YKW7ERlkJ37jmR"}
    tweets = requests.get(endpoint, headers=headers).json()

    tweetsPerQry = 100
    maxTweets = 100000000

    startDate = datetime.datetime(2019, 9, 15, 0, 0, 0) 
    endDate =   datetime.datetime(2020, 11, 16, 0, 0, 0)

    #### https://chatbotslife.com/crawl-twitter-data-using-30-lines-of-python-code-e3fece99450e #####

    # time = '2020-12-16'
    # tweets = api.GetSearch(raw_query="https://api.twitter.com/2/tweets/search/recent?query=snow&max_results=100")
    # data = tweets["data"]
    # token = tweets["meta"]["next_token"]
    # print(data)
    for hashtag in hashtags:
        maxId = -1
        tweetCount = 0
        while tweetCount < maxTweets:
            if(maxId <= 0):
                newTweets = api.search(q=hashtag, count=tweetsPerQry, result_type="recent", tweet_mode="extended")
            else:
                newTweets = api.search(q=hashtag, count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent", tweet_mode="extended")
            
            if not newTweets:
                print("no tweets for {}".format(hashtag))
                break
            
            for tweet in newTweets:
                print("tweets for {}".format(hashtag))
                print(tweet.created_at)
                if tweet.created_at < endDate and tweet.created_at > startDate:
                    cur.execute("INSERT INTO tweets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ("et_country(tweet.place)", tweet.full_text, get_hashtags(tweet.entities) , tweet.id,  tweet.user.id, tweet.lang, tweet.user.followers_count, tweet.retweet_count , tweet.user.verified, tweet.created_at))
                    conn.commit()
                # print(tweet.place)
                
            tweetCount += len(newTweets)	
            maxId = newTweets[-1].id

        
    # for hashtag in hashtags:
    # tweets = api.GetSearch(term="#IranInternetShutdown", count=7000, since="2019-11-15")
    # for tweet in tweets:
    #     data[tweet.created_at] = (tweet.text, tweet.geo)
    #     temp = extract_hashtags_from_tweets(tweet.text)
    #     for t in temp:
    #         if t not in extra_hashtags:
    #             extra_hashtags[t] = 1
    #         else:
    #             extra_hashtags[t] += 1
    #     # if tweet.create_at != start_date:
    #     cur.execute("INSERT INTO tweets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (get_country(tweet.place), tweet.text, '#'.join(temp), tweet.id,  tweet.user.id, tweet.lang, tweet.user.followers_count, tweet.retweet_count , tweet.user.verified, tweet.created_at))
    #     conn.commit()
    #     # new_datetime = datetime.strftime(datetime.strptime(tweet.created_at ,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d')
    #     # time = 
    # print(len(tweets))


    
    
if __name__ == "__main__":
    main()