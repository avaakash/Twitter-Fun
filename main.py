import json
import sys
from datetime import datetime, timedelta

from auth import authenticate
from update_banner import updateBanner
from image_util import create_image


def updateBannerNewFollower():

    api = authenticate()
    followers = api.followers()

    with open("last_update.json", "r") as f:
        last_update = json.load(f)
    current_update = {
        "id": followers[0].id_str,
        "time": datetime.now()
    }

    if last_update["id"] == current_update["id"]:
        if datetime.now() - datetime.strptime(last_update.get("time"), "%Y-%m-%d %H:%M:%S.%f") > timedelta(minutes=5):
            print("No update")
            updateBanner(api)
    else:
        create_image(followers[0].screen_name,
                     followers[0].profile_image_url_https)
        updateBanner(api, "new_welcome")
        with open("last_update.json", "w") as f:
            json.dump(current_update, f, default=str)


def main(arg):
    if arg == "follower-banner":
        updateBannerNewFollower()
    else:
        print("Not allowed")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        main("follower-banner")
    else:
        main(sys.argv[1])
