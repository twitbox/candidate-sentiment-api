import json
import os
import tweepy
from flask import jsonify

with open(os.path.realpath('secret/twitter.json')) as tokens_file:
  tokens = json.load(tokens_file)
  auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
  auth.set_access_token(tokens['access_token_key'], tokens['access_token_secret'])
  api = tweepy.API(auth)




def search(hashtag):
  print('Searching for the meaning of life in 140 characters')
  # Use 'since_id' parameter to ensure only newest tweets since last tweet
  res = api.search('#' + hashtag, count=100)
  for tweet in res:
    print(tweet.text)
    print(tweet.id)
  print(len(res))
  return 'OK'

