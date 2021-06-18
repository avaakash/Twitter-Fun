import sys

from auth import authenticate
from components.update_banner import updateBannerForNewFollower

def main(arg):
    api = authenticate()
    if arg == "follower-banner":
        updateBannerForNewFollower(api)
    else:
        print("Not allowed")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        main("follower-banner")
    else:
        main(sys.argv[1])
