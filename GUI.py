import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os
import json
from pytube.exceptions import VideoUnavailable
import sys
from PIL import Image, ImageTk



Mode = "Hallo"
dir = "None"


#set current dir
if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
elif __file__:
    current_dir = os.path.dirname(__file__)

#set folder and file (dir) path
folder_path = current_dir + '/Videos'
file_path = current_dir + "/dir.txt"

# function called to check if the dir file exist
def doesFileExists(filePathAndName):
    return os.path.exists(filePathAndName)

#checks if the folder Video exist, if not it creates one
if not os.path.exists(folder_path):
     os.makedirs(folder_path)

# check if file dir.txt exist, and create one. plus put in the right path
if doesFileExists(file_path):
  with open(file_path, 'r') as f:
    dir = json.load(f)
else:
  with open(file_path, 'w') as json_file:
    json.dump(file_path, json_file)

#sets dir to the place where the videos are going to be placed in.
dir = folder_path



#init app
root = tk.Tk()
root.title("Youtube Converter")
root.resizable(False, False)
root.geometry('500x500')
root.eval("tk::PlaceWindow . center")

#set Icon
ico = Image.open(r'C:\Users\domin\OneDrive\Desktop\wichtig\Programieren\VCS\yt Downloader\Icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)



def main():
    #Input form the text box
    link = link_entry.get()

    
    global yt
    global yd
    #checks if Links is filled
    if not link:
        messagebox.showwarning("Error", "Please enter a valid link.")
        return

    #tries to set yt to a link funtion from YT
    try: 
        yt = YouTube(link)
    except VideoUnavailable:
        messagebox.showwarning("Error", f'Video {link} is unavaialable.')
        return   
    #checks if yt is a valid link
    if yt == None:
        messagebox.showwarning("Error", "Invalid YouTube link or video is unavailable.")
        return
    
    #checks if the cobnvert is a video or a audio
    if Mode == "video":
        yd = yt.streams.get_highest_resolution()
    elif Mode == "audio":
        yd = yt.streams.get_audio_only()

    if yd == None:
        messagebox.showwarning("Error","No available streams for the highest resolution.")
        return

    yd.download(dir)
    link_entry.delete(0, tk.END)
    go_back()
    messagebox.showinfo("Complete","Download completed!""\n \n File saved in: \n" + dir)


def open_convert_window(selection):
    main_frame.pack_forget()
    convert_frame.pack()
    global Mode
    Mode = str(selection)

def go_back():
    convert_frame.pack_forget()
    main_frame.pack()


main_frame = tk.Frame(root)
convert_frame = tk.Frame(root)

#main_frame widget
Welcome_label = tk.Label(main_frame, text="Python Youtube Converter", font=("arial",25))
Welcome_label.pack(pady=20)

#tkinter picture rezise 50x50
img = Image.open(r'C:\Users\domin\OneDrive\Desktop\wichtig\Programieren\VCS\yt Downloader\Icon.png')
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)
panel = tk.Label(main_frame, image = img)
panel.pack(pady=20)



audio_button = tk.Button(main_frame, text="Audio", command=lambda: open_convert_window("audio"))
audio_button.pack(pady=20)

video_button = tk.Button(main_frame, text="Video", command=lambda: open_convert_window("video"))
video_button.pack(pady=20)

# Convert frame widgets
link_label = tk.Label(convert_frame, text="Enter the link:")
link_label.pack(pady=5)

link_entry = tk.Entry(convert_frame, width=40)
link_entry.pack(pady=5)

convert_button = tk.Button(convert_frame, text="Convert", command=main)
convert_button.pack(pady=10)

back_button = tk.Button(convert_frame, text="Back", command=go_back)
back_button.pack(pady=5)


# Pack the main frame
main_frame.pack()

#run app
root.mainloop()