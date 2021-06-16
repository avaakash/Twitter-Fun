
def updateBanner(api, banner="default"):
    if banner == "new_welcome":
        api.update_profile_banner("images/new_welcome_banner.jpg")
    elif banner == "default":
        api.update_profile_banner("images/default_banner.jpg")
    else:
        print("Banner not allowed")