import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
import os
from pytube.exceptions import VideoUnavailable
from PIL import Image, ImageTk
import sys
sys.path.append(os.getcwd()+'\\chache')
from cache.cache import *



switch_value = True


Mode = "None"
dir = "None"
iconDir = os.getcwd() + r"\assets\Icon.png"

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

light_open = Image.open("assets/light_mode.png")
light = ImageTk.PhotoImage(light_open)

dark_open = Image.open("assets/dark_mode.png")
dark = ImageTk.PhotoImage(dark_open)

# function called when converted started
def main():
    global yt
    global yd
    
    #Input form the text box
    link = link_entry.get()
    
    if get_default_dir() != "null":
        dir = get_default_dir()
    else: 
        dir = filedialog.askdirectory()

    if dir == "" or dir == None:
        messagebox.showwarning("Error", "Please select a directory.")
        return
    

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
    elif Mode == "playlist":
        print("playlist")
        #todo aufruf einer Funktion  welche die Playlist runterlädt 
        return

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

def set_def_dir():
    global def_dir
    def_dir = filedialog.askdirectory()
    if def_dir == "":
        messagebox.showwarning("Error", "Please select a directory.")
    else:
        update_default_dir(def_dir)

def toggle():
  
    global switch_value
    if switch_value == True:
        switch.config(image=light,bg="#26242f",
                      activebackground="#26242f")

        for frame in frame_list:
            frame.config(bg="#26242f")

        for button in button_list:
            button.config(bg="#26242f", fg="#ffffff", activebackground="#26242f", activeforeground="#ffffff")

        for extra in extra_list:
            extra.config(bg="#26242f", fg="#ffffff")
        
        switch_value = False
  
    else:
        switch.config(image=dark,bg="white", 
                      activebackground="white")
          
        for frame in frame_list:
            frame.config(bg="white")

        for button in button_list:
            button.config(bg="white", fg="#000000", activebackground="white", activeforeground="#000000")

        for extra in extra_list:
            extra.config(bg="white", fg="#000000")

        switch_value = True

main_frame = tk.Frame(root)
convert_frame = tk.Frame(root)
settings_frame = tk.Frame(root)

# ------ MAIN FRAME ------

settings_button = tk.Button(main_frame, text="⚙️", command=lambda: open_settings_window())
settings_button.pack(pady=10, padx=10, anchor=tk.NE)

#main_frame widget
Welcome_label = tk.Label(main_frame, text="PyConvert", font=("arial", 25))
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

playlist_button = tk.Button(main_frame, text="Playlist", command=lambda: open_convert_window("playlist"))
playlist_button.pack(pady=10)

# ------ CONVERT FRAME ------

link_label = tk.Label(convert_frame, text="Enter the link:")
link_label.pack(pady=5)

link_entry = tk.Entry(convert_frame, width=40)
link_entry.pack(pady=5)

convert_button = tk.Button(convert_frame, text="Convert", command=main)
convert_button.pack(pady=10)

back_button_Conv = tk.Button(convert_frame, text="Back", command=go_back)
back_button_Conv.pack(pady=5)

# ------ SETTINGS FRAME ------

back_button = tk.Button(settings_frame, text="Back", command=go_back)
back_button.pack()

switch = tk.Button(settings_frame, bd=0, bg="white",text="Light Mode", activebackground="white", command=toggle)
switch.pack(padx=50, pady=150)

def_folder_path = tk.Button(settings_frame, text="select default folder", command=lambda: set_def_dir())
def_folder_path.pack(pady=10)

reset_def_folder_path = tk.Button(settings_frame, text="reset default folder", command=lambda: clear_default_dir())
reset_def_folder_path.pack(pady=10)

# ------ PACKING ------
frame_list = [main_frame, convert_frame, settings_frame, root]
button_list = [back_button, back_button_Conv, settings_button, audio_button, video_button, convert_button,def_folder_path,reset_def_folder_path]
extra_list = [link_entry, link_label, panel, Welcome_label]


main_frame.pack()
toggle()
root.mainloop()