import json
import os
import tweepy

with open(os.path.realpath('secret/twitter.json')) as tokens_file:
  tokens = json.load(tokens_file)
  auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
  auth.set_access_token(tokens['access_token_key'], tokens['access_token_secret'])
  api = tweepy.API(auth)

def search():
  #tweepy.Cursor(api.search)
  print('Searching for the meaning of life in 140 characters')
