# Program to de-weebify Osu!
# Works by replacing background images in song folders with pictures downloaded from internet
# Also edits configuration to remove weeb settings

import urllib.request
import os

os.chdir(r'C:\Users\Christopher\AppData\Local\osu!\Songs')

url = 'https://www.pixelstalk.net/wp-content/uploads/2016/07/3D-Nature-Images-Free-Download.jpg'
# Download the file from `url` and save it locally under `file_name`:
# urllib.request.urlretrieve(url, 'file_name.jpg')

# walk through directories and list the files names
for dirname in os.listdir("."):
    if os.path.isdir(dirname):
        for i, filename in enumerate(os.listdir(dirname)):
            if (filename[-4:]) == ".jpg":
                print(filename)
            elif (filename[-4:]) == ".png":
                print(filename)

# check if song is tagges as anime
