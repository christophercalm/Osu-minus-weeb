# Program to de-weebify Osu!
# Works by replacing background images in song folders with pictures downloaded from internet
# Also edits configuration to remove weeb settings

import urllib.request
import os
import shutil
import random

project_path = os.getcwd()
nature_folder = project_path + "\\res\\images\\nature\\"

num_nature = 15

username = str(os.getlogin())
# default osu installation path
osu_path = "C:\\Users\\" + username + "\\AppData\\Local\\osu!\\Songs"
os.chdir(osu_path)



# Download the file from `url` and save it locally under `file_name`:


def get_background(folder):
    return folder + str(random.randrange(num_nature)) + ".jpg"
    # todo get number of files in folder


def delete_original(song_folder):
    try:
        os.remove(song_folder)
    except PermissionError as e:
        print(song_folder)
        print('Error: %s' % e.strerror)


def replace_file(src, dest):
    try:
        shutil.copy(src, dest)
    # Already moved
    except shutil.Error as e:
        print("That file already exists")
    # The source or destination does not exist
    except IOError as e:
        print(src)
        print(dest)
        print('Error: %s' % e.strerror)


def main():
    print("Backup your song folder before using this script...")
    contains_anime_tag = []
    # walk through directories and list the files names
    for dirname in os.listdir("."):
        if os.path.isdir(dirname):
            for i, filename in enumerate(os.listdir(dirname)):

                if (filename[-4:]) == ".jpg":
                    # delete_original(osu_path + '\\' + dirname + '\\' + filename)
                    replace_file(get_background(nature_folder),
                                 osu_path + '\\' + dirname + '\\' + filename)  # makes sure is jpg
                

# check if song is tagged as anime
# tv, anime, japanese
# see if beatmap backgrouns is supposexc to be a png from the .osu file. If it is then convert the file to a png or change the beatmap file.

main()
