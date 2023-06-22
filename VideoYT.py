from pytube import YouTube
from sys import argv
import time

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

link = argv[1]
yt = YouTube(link)
debug = False

if yt == None:
    print(color.RED + "Invalid YouTube link or video is unavailable." + color.END)
    time.sleep(5)
    exit()

print("\nTitle: ", yt.title)
print("\nViews: ", yt.views)



yd = yt.streams.get_highest_resolution()

if yd == None:
    print("No available streams for the highest resolution.")
    time.sleep(5)
    exit()



dir = r"C:\Users\domin\Videos\Captures"

Answer = input("Do you want to download this video? (y/n)\n" + yt.title)
if Answer == "y":
    print(color.GREEN + "\nDownloading...\n" + color.END)
else:
    exit()


yd.download(dir)
print(color.GREEN + "Download completed!" + color.END + " File saved in: " + color.UNDERLINE + dir + color.END)
