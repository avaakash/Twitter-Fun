import urllib.request
from PIL import Image, ImageFont, ImageDraw

import settings

# Downloading an image from a url and saving it as per needs
def download_image(url, filename):
    urllib.request.urlretrieve(url, settings.generated(f"images/{filename}.png"))

# The function which creates the cover photo for us
def create_image(screen_name, profile_photo):
    fontsize = 1  # starting font size
    img_fraction = 0.45 # how much percentage width should the text be 
    download_image(profile_photo, "user_image")
    user_image = Image.open(settings.generated("images/user_image.jpg"))
    welcome_image = Image.open(settings.static("images/welcome.jpg"))
    text = str(screen_name)
    image_editable = ImageDraw.Draw(welcome_image)

    # Setting font size
    font = ImageFont.truetype(settings.static("fonts/playfair.ttf"), fontsize)
    while font.getsize(text)[0] < img_fraction*welcome_image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(settings.static("fonts/playfair.ttf"), fontsize)
    print(fontsize)

    # Write the text and paste the user image to our cover image
    image_editable.text((490, 180), text, (0, 0, 0), font=font)
    user_image = user_image.resize((90, 90))
    welcome_image.paste(user_image, (390, 185))
    welcome_image.save(settings.generated("images/new_welcome_banner.jpg"))
