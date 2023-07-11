from pytube import YouTube
import time
import os
import json
from pytube.exceptions import VideoUnavailable
import sys

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# deklare dir
dir = "None"

#set current dir
if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
elif __file__:
    current_dir = os.path.dirname(__file__)

#set folder and file (dir) path
folder_path = current_dir + '\Videos'
file_path = current_dir + "\dir.txt"

# function called to check if the dir file exist
def doesFileExists(filePathAndName):
    return os.path.exists(filePathAndName)


# check if file dir.txt exist, and create one. plus put in the right path
if doesFileExists(file_path):
  with open(file_path, 'r') as f:
    dir = json.load(f)
else:
  with open(file_path, 'w') as json_file:
    dir = json.dump(folder_path, json_file)
    
#checks if the folder Video exist, if not it creates one
if not os.path.exists(dir):
    os.makedirs(dir)


#main function that runs the converter
def main():
    link = input(color.GREEN + "\nplease enter a Youtube URL\n\n" + color.END)

    try: 
        yt = YouTube(link)
    except VideoUnavailable:
            print(f'Video {link} is unavaialable, skipping.')   

    if yt == None:
        print(color.RED + "Invalid YouTube link or video is unavailable." + color.END)
        time.sleep(5)
        exit()
# bug yt. unbound 
    print("\nTitle: ", yt.title)
    print("\nViews: ", yt.views)

#chypher code ändern 

    yd = yt.streams.get_highest_resolution()

    if yd == None:
        print(color.RED + "No available streams for the highest resolution." + color.END)
        time.sleep(5)
        exit()


    Answer = input("\nDo you want to download this video? (y/n)\n")
    if Answer.lower() == "y":
        print(color.GREEN + "\nDownloading...\n" + color.END)
    else:
        exit()


    yd.download(dir)
    print(color.GREEN + "Download completed!" + color.END + " File saved in: " + color.UNDERLINE + dir + color.END)

    again = input("\nDo you want to download another video? (y/n)\n")
    if again.lower() == "y":
        main()
    else:
        print(color.PURPLE + "\n \nmade by LoLFuchs" + color.END)
        time.sleep(3)
        exit()

main()
