import random
import urllib.request


def image_downloader(url):
    name = random.randrange(1, 100)
    img_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, img_name)


# image_downloader('https://pbs.twimg.com/profile_images/814773510988038145/n3p8dsIL_400x400.jpg')
image_downloader('file:///Volumes/LEYNILSON/LeynilsonThe1st/ceevee/images/portfolio/modals/m-girl.jpg')
