from PIL import Image, ImageFont, ImageDraw, ImageFilter
import urllib.request

def download_image(url):
    urllib.request.urlretrieve(url, "images/user-image.jpg")

def create_image(username, profile_photo):
    fontsize = 1  # starting font size
    img_fraction = 0.40
    download_image(profile_photo)
    user_image = Image.open("images/user-image.jpg")
    welcome_image = Image.open("images/welcome.jpg")
    text = str(username)
    image_editable = ImageDraw.Draw(welcome_image)

    # Setting font size
    font = ImageFont.truetype("fonts/playfair.ttf", fontsize)
    while font.getsize(text)[0] < img_fraction*welcome_image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("fonts/playfair.ttf", fontsize)

    print(fontsize)
    # Update Image
    image_editable.text((490, 180), text, (0, 0, 0), font=font)
    user_image = user_image.resize((90, 90))
    welcome_image.paste(user_image, (390, 185))
    welcome_image.save("images/new_welcome_banner.jpg")


create_image("_avaakash_",
             "https://pbs.twimg.com/profile_images/879627513659621376/PS72sTUq_normal.jpg")
