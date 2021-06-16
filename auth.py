import tweepy
from env_util import getEnv

def authenticate():
    environ_secrets = getEnv()
    consumer_key = environ_secrets[0]
    consumer_secret = environ_secrets[1]
    access_token = environ_secrets[2]
    access_token_secret = environ_secrets[3]

    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        return api
    except:
        return None
