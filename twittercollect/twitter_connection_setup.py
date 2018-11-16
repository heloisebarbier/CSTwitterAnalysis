import tweepy
# We import our access keys:
from tweet_collection.credentials import *

# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = 'sAkOULOPAWjRMzvSx7gvSfefb'
CONSUMER_SECRET = 'KQZBAjwRXLs3tTUoLfANAuyyyTPgVdlDWy2QPXfBhJZWKOOYcx '

# Access:
ACCESS_TOKEN  = '1062337478613495808-wsZAMFdm3ANLFcn6U2MjMEJOaYvZQR'
ACCESS_SECRET = 'TZWC8EofdGdqyD5FSpSYABdL1uRTQoIZTmv6g0y5chQRR'

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api
