import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import threading

root = Tk()
root.title("mp3 Video Player")
root.geometry("485x700+290+10")
root.configure(background='#333333')
root.resizable(False, False)
root.update()

mixer.init()

# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)
       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)



def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    
    def play_music_thread():
        mixer.music.load(Playlist.get(ACTIVE))
        mixer.music.play()
        
    threading.Thread(target=play_music_thread).start()


image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)


# count for gif
frameCnt = 30
frames = [PhotoImage(file='bg.gif',height= 520,width = 485,format = 'gif -index %i' %(i)) for i in range(frameCnt)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
    
    
    
    
    
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)

# icon
lower_frame = Frame(root , bg = "#FFFFFF", width = 485 , height = 180 )
lower_frame.place ( x = 0 , y = 400)

# Button
ButtonPlay = PhotoImage(file="play.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height = 60, width =60,command=PlayMusic).place(x=215, y=487)

ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height = 60, width =60,command=mixer.music.stop).place(x=130, y=487)

Buttonvolume = PhotoImage(file="volume.png")
Button(root, image=Buttonvolume, bg="#FFFFFF", bd=0, height = 60, width =60,command=mixer.music.get_volume).place(x=20, y=487)

ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height = 60, width =60,command=mixer.music.pause).place(x=300, y=487)

# Label       
# white image to place buttons on it
Menu = PhotoImage(file="menu1.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)


Button(root, text="Browse Music", width=59, height=1, font=("calibri",12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# Execute Tkinter
root.mainloop()