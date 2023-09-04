import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
import os
from pytube.exceptions import VideoUnavailable
from PIL import Image, ImageTk



Mode = "None"
dir = "None"
iconDir = os.getcwd() + r"\Icon.png"
print(iconDir)

#init app
root = tk.Tk()
root.title("Youtube Converter")
root.resizable(False, False)
root.geometry('500x500')
root.eval("tk::PlaceWindow . center")

#set Icon
ico = Image.open(iconDir)
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)



# function called when converted started
def main():
    #Input form the text box
    link = link_entry.get()
    dir = filedialog.askdirectory()

    if dir == "":
        messagebox.showwarning("Error", "Please select a directory.")
        return
    
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
    
    #checks if the convert is a video or a audio
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


def open_settings_window():
    main_frame.pack_forget()
    settings_frame.pack()

def open_convert_window(selection):
    main_frame.pack_forget()
    convert_frame.pack()
    global Mode
    Mode = str(selection)

def go_back():
    link_entry.delete(0, tk.END)
    convert_frame.pack_forget()
    settings_frame.pack_forget()
    main_frame.pack()




main_frame = tk.Frame(root)
convert_frame = tk.Frame(root)
settings_frame = tk.Frame(root)

# ------ MAIN FRAME ------

settings_button = tk.Button(main_frame, text="⚙️", command=lambda: open_settings_window())
settings_button.pack(pady=10, padx=10, anchor=tk.NE)

#main_frame widget
Welcome_label = tk.Label(main_frame, text="Python Youtube Converter", font=("arial", 25))
Welcome_label.pack(pady=20, padx=10, anchor=tk.NE)

#tkinter picture rezise 50x50
img = Image.open(iconDir)
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)
panel = tk.Label(main_frame, image=img)
panel.pack(pady=20)

audio_button = tk.Button(main_frame, text="Audio", command=lambda: open_convert_window("audio"))
audio_button.pack(pady=10)

video_button = tk.Button(main_frame, text="Video", command=lambda: open_convert_window("video"))
video_button.pack(pady=10)

# ------ CONVERT FRAME ------

link_label = tk.Label(convert_frame, text="Enter the link:")
link_label.pack(pady=5)

link_entry = tk.Entry(convert_frame, width=40)
link_entry.pack(pady=5)

convert_button = tk.Button(convert_frame, text="Convert", command=main)
convert_button.pack(pady=10)

back_button = tk.Button(convert_frame, text="Back", command=go_back)
back_button.pack(pady=5)

# ------ SETTINGS FRAME ------

back_button = tk.Button(settings_frame, text="Back", command=go_back)
back_button.pack()

main_frame.pack()

root.mainloop()