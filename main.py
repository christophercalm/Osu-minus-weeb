##Program to de-weebify Osu!

import urllib.request
import os

url = 'https://www.pixelstalk.net/wp-content/uploads/2016/07/3D-Nature-Images-Free-Download.jpg'
# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(url, 'file_name.jpg')

# walk through directories and list the files names
for dirname in os.listdir("."):
    if os.path.isdir(dirname):
        for i, filename in enumerate(os.listdir(dirname)):
            if (filename[-4:]) == ".png" or ".jpg":
                print("hello world")
