import tweepy
from utils.env_util import getEnv

def authenticate():
    # Getting the tokens and keys
    environ_secrets = getEnv()
    # Setting up variables
    consumer_key = environ_secrets[0]
    consumer_secret = environ_secrets[1]
    access_token = environ_secrets[2]
    access_token_secret = environ_secrets[3]

    # Creating Auth object
    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    # Setting access token to access API
    auth.set_access_token(access_token, access_token_secret)

    # Getting the API object to make API calls
    api = tweepy.API(auth)

    # Verifying API and returning the API object
    try:
        api.verify_credentials()
        print("Verified")
        return api
    except:
        print("Wrong Credentials")
        return None
