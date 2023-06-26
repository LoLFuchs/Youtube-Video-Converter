from pytube import YouTube
import time
import os
import json

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


dir = "None"

current_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = current_dir + '/Videos'
file_path = current_dir + "/dir.txt"

def doesFileExists(filePathAndName):
    return os.path.exists(filePathAndName)

if not os.path.exists(folder_path):
     os.makedirs(folder_path)

# Example
if doesFileExists(file_path):
  with open(file_path, 'r') as f:
    dir = json.load(f)
else:
  with open(file_path, 'w') as json_file:
    json.dump(file_path, json_file)

dir = folder_path


debug = False
def main():
    link = input(color.GREEN + "\nplease enter a Youtube URL\n" + color.END)
    yt = YouTube(link)

    if yt == None:
        print(color.RED + "Invalid YouTube link or video is unavailable." + color.END)
        time.sleep(5)
        exit()

    print("\nTitle: ", yt.title)
    print("\nViews: ", yt.views)



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
