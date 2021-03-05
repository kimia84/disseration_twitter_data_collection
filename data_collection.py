import requests
import os
import json
from dotenv import load_dotenv
import psycopg2
import time
from pathlib import Path 
import twitter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
bearer_token = str(os.getenv('BEARER_TOKEN'))

start_date = "201909150000" # from 15th september 2019
end_date = "202012150000" # until 15th december 2020

url = "https://api.twitter.com/1.1/tweets/search/fullarchive/staging.json"
    
# tweet.user.followers_count, tweet.retweet_count , tweet.user.verified, 

#### connect to database to store our data - https://www.psycopg.org/docs/install.html#quick-install ####
def connect_to_postgres():
    # Connect to your postgres DB
    try:
        conn = psycopg2.connect("host=localhost dbname=twitterData user=kimiapirouzkia")
    except:
        print("Unable to connect to the associates database.")

    # Open a cursor to perform database operations
    cur = conn.cursor()
    return conn, cur

#### https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/ ####
def extract_initial_hashtags_from_text_file():
    hashtags = []
    f = open("hashtags.txt", "r")
    for line in f:
        hashtags.append(str(line.strip()))
    f.close()
    
    return hashtags

def get_country(place):
    if not place:
        return "N/A"
    
    return place["country"]

def create_headers(token):
    headers = {"Authorization":"Bearer {}".format(token),
               "content-type":"application/json",
               }
    
    return headers

def connect_to_endpoint(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code)
    
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    
    return response.json()

def collect_all(url, hashtags):
    token = bearer_token
    
    next_token = ''
    
    for hashtag in hashtags:
        while True:
            conn, cur = connect_to_postgres()
            
            payload = {
                    "query":hashtag,
                    "maxResults":"500",
                    "fromDate":start_date,
                    "toDate":end_date,
                    }
            
            if next_token:
                payload['next'] = next_token
                
            tweets = connect_to_endpoint(url, create_headers(token), payload)
            
            results = tweets['results']
            
            if results:
                print("there ARE tweets for {}".format(hashtag))
                
                for tweet in results:
                    try:
                        cur.execute("INSERT INTO tweets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (json.dumps(get_country(tweet['place'])), json.dumps(tweet['text']), json.dumps(tweet['entities']['hashtags']), json.dumps(tweet['id']),  json.dumps(tweet['user']['id']), json.dumps(tweet['lang']), json.dumps(tweet['user']['followers_count']), json.dumps(tweet['retweet_count']) , json.dumps(tweet['user']['verified']), json.dumps(tweet['created_at']), json.dumps(tweet['favorite_count'])))
                        
                        conn.commit()
                    except Exception as e:
                        print("tweet id: {} - error: {}".format(tweet['id'], e))
                        pass
                    
                if 'next' in tweets:
                    next_token = tweets['next']  
                else: 
                    print("no next token so we move to the next hashtag")
                    break
                
            else:
                print("there are NO tweets for {}".format(hashtag))
                break
                
            print("sleeping for 10 secs")
            time.sleep(10)
            

def main():
    hashtags = extract_initial_hashtags_from_text_file()
    
    collect_all(url, hashtags)


if __name__ == "__main__":
    main()