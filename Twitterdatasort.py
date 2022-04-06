import time
import tweepy
import configparser
import pandas as pd
import requests
from requests.exceptions import MissingSchema


# configparser  for read files
config = configparser.ConfigParser()
config.read('config.ini')
# twitter app details
app_key = 'BGpC3UyTuajGOB7KJqikJZqpq'
app_secret = 'qYHfOXpKTIlWlrNUePtTRtn9xgJJwlgX4NUpSUShpuZPDb5mET'
access_token = '1502851009994919938-H455qJzUD8Y45NTG33SOdYVpxipz9a'
access_token_key = 'yVWfsHmfJOfV6ddHniBxFH3mFIVGfrGNmgKrHm20o4Di6'

# authorization and accessing keys
authority = tweepy.OAuthHandler(app_key, app_secret)
authority.set_access_token(access_token, access_token_key)

# calling the api
api = tweepy.API(authority, wait_on_rate_limit=True)
# page
user = 'Calendly'
limit = 20000
followers = tweepy.Cursor(api.get_followers, screen_name=user, count=200).items(limit)

columns = ['user_id', 'name', 'screen name', 'country', 'website','bio', 'follower count', 'following count', 'Latest tweet']
row = []

def unrolled_url():
    url = followers.url
    site = requests.head(url,allow_redirects=False,verify= True)
    try:
        a = site.url
    except MissingSchema:
        pass
    return a

def latest_tweet():
    status = api.get_status(user)
    status.created_at = latest_tweet
    print(latest_tweet)
try:
    for x in followers:
        row.append([x.id,x.name,x.screen_name,x.location,unrolled_url,x.description,x.followers_count,x.friends_count,latest_tweet])
except :
    time.sleep(60)
df = pd.DataFrame(row, columns = columns)

df.to_csv('datasoorting.csv')

