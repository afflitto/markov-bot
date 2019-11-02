import tweepy
import config
import json
import argparse
import re

# set up parser
parser = argparse.ArgumentParser(description="Downloads a user's tweets as a json file")
parser.add_argument('username', action="store", help='username of the twitter account you want to download')
parser.add_argument('--include-mentions', action="store_true", dest="include_mentions", default=False, help='include @mentions in tweet output')
parser.add_argument('--mentions_mode', action="store", default="strip", help="strip: remove @mentions (default)\nremove@: remove only the @ sign\nignore: do nothing")
parser.add_argument('--rt_mode', action="store", default="strip", help='strip: remove "RT" characters (default)\nignore: do nothing')
args = parser.parse_args()

# set up Tweepy API
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key, config.access_secret)
api = tweepy.API(auth)

output = open("tweets-"+args.username+".json", "w+") # open output file
tweets = [] # list to hold the saved tweets

for tweet in tweepy.Cursor(api.user_timeline, id=args.username, tweet_mode="extended").items(): # For each tweet in user's timeline
    tweet_text = tweet.full_text.encode('utf8') # save UTF-8 encoded text
    if not args.include_mentions:
        tweet_text = re.sub(r'@\w*', '', tweet_text) # remove @mentions
    if "RT" not in tweet_text and "http" not in tweet_text:
        tweets.append(tweet_text) # add to list if the tweet is not a retweet and has no links

json.dump(tweets, output) # save to file
