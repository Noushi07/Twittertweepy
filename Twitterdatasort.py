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
    for follow in followers:
      try:
        a=(follow.url)
        site = requests.get(url=a,allow_redirects=True)
        url=(site.url)
        return url
      except (MissingSchema,requests.exceptions.ConnectionError):
          url_null=('None')
          return url_null
          pass

def latest_tweet():
  for follower in followers:
    try:
       tweet=(follower.status.created_at)
       return tweet
    except AttributeError:
        tweet_null=('None')
        return tweet_null
        pass
    
for follow in followers:
    a=latest_tweet()
    b=unrolled_url()
    row.append([follow.id,follow.name,follow.screen_name,follow.location,b,follow.followers_count,follow.friends_count,a,follow.description])
    
df = pd.DataFrame(row, columns = columns)

df.to_csv('Datacalendly.csv')

