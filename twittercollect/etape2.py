import tweepy
from twittercollect import twitter_connection_setup

def collect_by_user(user_id):
    connexion = twitter_connection_setup.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

print(collect_by_user())
