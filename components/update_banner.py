import json
import settings
from datetime import datetime, timedelta


from utils.image_util import create_image


def updateBannerForNewFollower(api):

    # Getting the followers list
    followers = api.followers()

    # Getting the last updated data
    with open(settings.data("last_update.json"), "r") as f:
        last_update = json.load(f)
    # Latest update from the api call
    current_update = {
        "id": followers[0].id_str,
        "time": datetime.now()
    }
    # Deserializing the time from the json into datetime format
    last_updated_time = datetime.strptime(
        last_update.get("time"), "%Y-%m-%d %H:%M:%S.%f")
    
    # Checking if there has been a new follower or not
    # Updating the banner if there hasn't been any new follower in last
    # 5 minutes or updating the banner with the new follower
    # if there is a new follower
    if last_update["id"] == current_update["id"]:
        if datetime.now() - last_updated_time > timedelta(minutes=5):
            print("No update")
            api.update_profile_banner(settings.static("images/default_banner.jpg"))
    else:
        create_image(followers[0].screen_name,
                     followers[0].profile_image_url_https)
        api.update_profile_banner(settings.generated(
            "images/new_welcome_banner.jpg"))
        # Saving the latest data back into the json file
        with open(settings.data("last_update.json"), "w") as f:
            json.dump(current_update, f, default=str)
