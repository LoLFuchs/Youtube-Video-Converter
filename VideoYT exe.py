from pytube import YouTube
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



    dir = r""

    Answer = input("\nDo you want to download this video? (y/n)\n")
    if Answer == "y" or "Y":
        print(color.GREEN + "\nDownloading...\n" + color.END)
    else:
        exit()


    yd.download(dir)
    print(color.GREEN + "Download completed!" + color.END + " File saved in: " + color.UNDERLINE + dir + color.END)

    again = input("\nDo you want to download another video? (y/n)\n")
    if again == "y" or "Y":
        main()
    else:
        print(color.PURPLE + "\n \nmade by LoLFuchs" + color.END)
        time.sleep(3)
        exit()

main()
