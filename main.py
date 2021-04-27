import tweepy
import pandas as pd

consumer_key = "your key"
consumer_secret = "your secret"
access_token = "your token"
access_token_secret = "your token secret"

tweets = []
retweets = []
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

cursor = tweepy.Cursor(
    api.user_timeline, id='handle of the user', tweet_mode="extended").items(10)
for i in cursor:
    print(i.full_text)
    print("\n")
input("press any key to exit")
