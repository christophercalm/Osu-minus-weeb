# Program to de-weebify Osu!
# Works by replacing background images in song folders with pictures downloaded from internet
# Also edits configuration to change settings

import os
import shutil
import random
from PIL import Image
from os.path import splitext
import click


project_path = os.getcwd()
nature_folder = project_path + "\\res\\images\\nature\\"

num_nature = 15

username = str(os.getlogin())
# default osu installation path
osu_song_path = "C:\\Users\\" + username + "\\AppData\\Local\\osu!\\Songs"
os.chdir(osu_song_path)


def get_background(folder, ext):
    return folder + str(random.randrange(num_nature)) + ext
    # todo get number of files in folder
    # todo make this sequential instead of random\


def replace_file(src, dest):
    try:
        shutil.copy(src, dest)
    # Already moved
    except shutil.Error as e:
        click.echo("That file already exists")
    # The source or destination does not exist
    except IOError as e:
        click.echo(src)
        click.echo(dest)
        click.echo('Error: %s' % e.strerror)


def is_background(image_path):
    if image_path[-4:] == ".jpg" or image_path[-4:] == ".png":
        with Image.open(image_path) as img:
            width, height = img.size
            if width * height >= 20000:  # 500 * 400 pixels. This is low to make sure all backgrounds are replaced
                return True
            else:
                return False
    else:
        return False


def change_preferences(config_file, turn_off_seasonal, turn_off_song_skin, turn_off_thumbnails):
    with open(config_file, 'r') as file:
        # read a list of lines into data
        data = file.readlines()
    for i in range(len(data)):

        if turn_off_seasonal and "Seasonal" in data[i]:
            data[i] = data[i][:21] + " Never\n"
        if turn_off_song_skin and "IgnoreBeatmapSkins" in data[i]:
            data[i] = data[i][:-2] + "1\n"
        if turn_off_thumbnails and "SongSelectThumbnails" in data[i]:
            data[i] = data[i][:-2] + "0\n"
    # and write everything back
    with open(config_file, 'w') as file:
        file.writelines(data)


# command line options
@click.command()
@click.option('-backgrounds', default=0,
              help='0 to keep backgrounds, 1 to replace with nature images')
@click.option('-seasonal', is_flag=True,
              help='Remove seasonal images?')
@click.option('-thumbnails', is_flag=True,
              help='Hide thumbnails?')
@click.option('-skins', is_flag=True,
              help='Disable song skins?')
def main(backgrounds, seasonal, thumbnails, skins):

    # go up a directory to change file in root colder
    os.chdir('..')
    change_preferences("osu!." + username + ".cfg", seasonal, skins, thumbnails)

    # change back
    os.chdir(osu_song_path)

    click.echo("Backup your song folder before using this script...")
    continue_script = input("This script may corrupt your beatmaps and delete files. Do you want to continue? y/n): ")

    contains_anime_tag = []
    # walk through directories and list the files names
    if backgrounds != 0 and continue_script.lower() == 'y':
        for dirname in os.listdir("."):
            if os.path.isdir(dirname):
                click.echo(dirname)
                for i, file in enumerate(os.listdir(dirname)):
                    filename, extension = splitext(file)
                    if is_background(osu_song_path + '\\' + dirname + '\\' + file):
                        click.echo(file)
                        replace_file(get_background(nature_folder, extension),
                                     osu_song_path + '\\' + dirname + '\\' + file)

    click.echo("Done!")
# check if song is tagged as anime
# tv, anime, japanese
# see if beatmap backgrounds is supposed to be a png from the .osu file.
# If it is then convert the file to a png or change the beatmap file.
main()
