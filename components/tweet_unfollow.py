import json

from auth import authenticate

def tweetUnfollow():
    api = authenticate()
    with open("last_update.json", "r") as f:
        last_update = json.load(f)
    
    