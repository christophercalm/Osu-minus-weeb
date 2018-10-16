# Program to de-weebify Osu!
# Works by replacing background images in song folders with pictures downloaded from internet
# Also edits configuration to remove weeb settings

import os
import shutil
import random
from PIL import Image
from os.path import splitext
import fileinput
import sys

project_path = os.getcwd()
nature_folder = project_path + "\\res\\images\\nature\\"

num_nature = 15
seasonal_backgrounds_line = 123
beatmap_skin_line = 58
thumbnail_line = 110

username = str(os.getlogin())
# default osu installation path
osu_song_path = "C:\\Users\\" + username + "\\AppData\\Local\\osu!\\Songs"
os.chdir(osu_song_path)


def get_background(folder, ext):
    return folder + str(random.randrange(num_nature)) + ext
    # todo get number of files in folder


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


def is_background(image_path):
    if image_path[-4:] == ".jpg" or image_path[-4:] == ".png":
        with Image.open(image_path) as img:
            width, height = img.size
            if width * height >= 480000:  # 800 * 600 pixels
                return True
            else:
                return False
    else:
        return False


def get_preferences():
    get_seasonal = False
    get_song_skin = False
    get_turn_off_thumbnails = False
    seasonal_str = str(input("Do you want to turn off Seasonal Images? Yes/No: "))
    if seasonal_str.lower() == "yes":
        get_seasonal = True
    song_skin_str = str(input("Do you want to ignore song skins? Yes/No: "))
    if song_skin_str.lower() == "yes":
        get_song_skin = True
    turn_off_thumbnails_str = str(input("Do you want to turn off thumbnails?? Yes/No: "))
    if turn_off_thumbnails_str.lower() == "yes":
        get_turn_off_thumbnails = True
    return get_seasonal, get_song_skin, get_turn_off_thumbnails


def change_preferences(config_file, seasonal, song_skin, turn_off_thumbnails):
    with open(config_file, 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    if seasonal:
        # deletes final characters and changes setting
        data[seasonal_backgrounds_line] = data[seasonal_backgrounds_line][:-6] + "Never\n"
    if song_skin:
        data[beatmap_skin_line] = data[beatmap_skin_line][:-2] + "1\n"
    if turn_off_thumbnails:
        data[thumbnail_line] = data[thumbnail_line][:-2] + "1\n"

    # and write everything back
    with open(config_file, 'w') as file:
        file.writelines(data)


def main():
    seasonal = False
    song_skin = False
    turn_off_thumnails = False
    change_preferences_test = str(input("Do you want to change preferences? Yes/No"))

    # go up a directory to change file in root colder
    os.chdir('..')
    if change_preferences_test.lower() == "yes":
        seasonal, song_skin, turn_off_thumbnails = get_preferences()
        change_preferences("osu!." + username + ".cfg", seasonal, song_skin, turn_off_thumbnails)

    # change back
    os.chdir(osu_song_path)

    print("Backup your song folder before using this script...")
    contains_anime_tag = []
    # walk through directories and list the files names
    for dirname in os.listdir("."):
        if os.path.isdir(dirname):
            for i, file in enumerate(os.listdir(dirname)):
                filename, extension = splitext(file)
                if is_background(osu_song_path + '\\' + dirname + '\\' + file):
                    # delete_original(osu_path + '\\' + dirname + '\\' + filename)
                    replace_file(get_background(nature_folder, extension), osu_song_path + '\\' + dirname + '\\' + file)

                
# check if song is tagged as anime
# tv, anime, japanese
# see if beatmap backgrounds is supposed to be a png from the .osu file.
# If it is then convert the file to a png or change the beatmap file.

main()
