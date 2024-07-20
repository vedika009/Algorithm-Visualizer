from multiprocessing.connection import wait
import tkinter as tk
import fnmatch
import os
import sys
from pygame import mixer 
import random 
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import threading
from PIL import Image
import pystray
from pystray import MenuItem as item

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("Logo.png")
canvas = tk.Tk()
canvas.title("FlacoPlayer")
canvas.geometry("400x500")
canvas.config(bg = 'black')
path = [resource_path("Music1") ,resource_path("Music2")] 
pattern = ["*.flac", "*.mp3"]
randompath = random.choice(path)
#mixer.init()

prev_img = tk.PhotoImage(file=resource_path("assets\\prev_img.png"))
stop_img = tk.PhotoImage(file=resource_path("assets\\stop_img.png"))
play_img = tk.PhotoImage(file=resource_path("assets\\play_img.png"))
pause_img = tk.PhotoImage(file=resource_path("assets\\pause_img.png"))
next_img = tk.PhotoImage(file=resource_path("assets\\next_img.png"))
music = tk.PhotoImage(file=resource_path("assets\\music.png"))
Logo = resource_path("assets\\icon.ico")
icon = tk.PhotoImage(file=resource_path("assets\\music-notes.png"))
canvas.iconphoto(False, icon)


listBox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100, font = ('poppins', 10))
listBox.pack(padx = 15, pady = 15)

global not_play
def donot_play():
    global not_play
    not_play=True
    #print(not_play)

def auto():
    global not_play
    not_play=False
    #print(not_play)

def auto_play():
    auto()

def select ():
    mixer.init()
    path=randompath
    files=os.listdir(path)
    global d
    d=random.choice(files)
    label.config(text = d + '\n' + "/")
    time.sleep(0.1)
    label.config(text = d + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = d + '\n' +"/")
    time.sleep(0.1)
    label.config(text = d + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = d + '\n' + "/")
    time.sleep(0.1)
    label.config(text = d + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = d + '\n' +"/")
    time.sleep(0.1)
    label.config(text = d + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = d + '\n' +"\\")
    win = randompath + "\\" + d
    mixer.music.load(win)
    mixer.music.play()
    os.chdir(randompath)
    a = mixer.Sound(d)
    timing = float(a.get_length())
    new=(round(timing, 2))
    new_temp=(new//60)
    new_t=str(new_temp)
    label.config(text = d + '\n' + new_t.replace(".0","") + ":" + str(round(timing%60,0)).replace(".0",""))     
    len=a.get_length()
    time.sleep(len)
    
    if not mixer.music.get_busy():
        #print("Control Given")
        if not_play==False:
            #print("next")
            threading.Thread(target=select).start()           
        else:
            print("Auto-Play turned off")
    else:
        print("song is currently active!")

def auto_off():
    donot_play()
  
def stop():
    donot_play()
    #canvas.destroy()
    mixer.music.stop()
    mixer.quit()
    listBox.select_clear('active')

def play_next():
    mixer.init()
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name + '\n' + "/")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"/")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' + "/")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"/")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    mixer.music.load(randompath + "\\" + next_song_name)
    mixer.music.play()
    b= mixer.Sound(next_song_name)
    next_timing = (b.get_length())
    tn=int(next_timing)
    label.config(text = next_song_name + '\n' + str(int(tn/60)) + " min")
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    mixer.init()
    next_song = listBox.curselection()
    #time.sleep(5)
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)
    label.config(text = next_song_name + '\n' + "/")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"/")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' + "/")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"/")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    time.sleep(0.1)
    label.config(text = next_song_name + '\n' +"\\")
    mixer.music.load(randompath + "\\" + next_song_name)
    mixer.music.play()
    b= mixer.Sound(next_song_name)
    next_timing = (b.get_length())
    tn=int(next_timing)
    label.config(text = next_song_name + '\n' + str(int(tn/60)) + " min")
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pauseButton['text'] == "Pause":
        mixer.music.pause()
        pauseButton['text'] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


def show_win(icon, item):
    icon=icon.stop()
    canvas.after(0,canvas.deiconify())

def quit_music(icon):
    
    icon=icon.stop()
    canvas.after(0,canvas.deiconify())
    #mixer.music.stop()
    canvas.destroy()



def mini():
    canvas.withdraw()
    #threading.Thread(target=select).start()
    image=Image.open(resource_path("assets\\music.png"))
    menu=(item('Play/Pause', pause_song),item('Auto-off', auto_off),item('Auto-On', auto_play),item('Random',lambda:threading.Thread(target=select).start(),default=True), item('Restore', show_win),item('STOP', stop),item('Quit', quit_music))
    if not_play==True:
        tray="Auto-play OFF"
    else:
        tray="Auto-Play ON"
    icon=pystray.Icon("name", image, "{}".format(tray), menu=menu)
    icon.run()

label = tk.Label(canvas, text = '', bg= 'black', fg = 'yellow', font = ('poppins',10))
label.pack(pady = 15)

top = tk.Frame(canvas, bg ='black')
top.pack(padx=10, pady=5, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", image = prev_img, bg = 'black', borderwidth = 0, command = lambda:threading.Thread(target=play_prev).start())
prevButton.pack(padx=5,pady = 30, in_= top, side = 'left')

pauseButton = tk.Button(canvas, text = "pause", image = pause_img, bg = 'black', borderwidth = 0, command= pause_song)
pauseButton.pack(padx=5,pady = 30, in_= top, side = 'left')


nextButton = tk.Button(canvas, text = "next", image = next_img, bg = 'black', borderwidth = 0, command = lambda:threading.Thread(target=play_next).start())
nextButton.pack(padx=5,pady = 30, in_= top, side = 'left')


stopButton = tk.Button(canvas, text = "Stop", image = stop_img, bg = 'black', borderwidth = 0, command = stop)
stopButton.pack(padx=5,pady = 30, in_= top, side = 'left')


playButton = tk.Button(canvas, text = "play", image = play_img, bg = 'black', borderwidth = 0, command= lambda:threading.Thread(target=select).start() )
playButton.pack(padx=5,pady = 30, in_= top, side = 'left')

def minimise():
    canvas.withdraw()    
    image=Image.open(resource_path("assets\\music.png"))
    menu=(item('Play/Pause', pause_song),item('Auto-off', auto_off),item('Auto-On', auto_play),item('Random',lambda:threading.Thread(target=select).start()), item('Restore', show_win),item('STOP', stop,default=True),item('Quit', quit_music))
    if not_play==True:
        tray="Auto-play OFF"
    else:
        tray="Auto-Play ON"
    icon=pystray.Icon("name", image, "{}".format(tray), menu=menu)
    icon.run()



addtray = tk.Button(canvas, text = "mini", image = music, bg = 'black',borderwidth=0, command= lambda:threading.Thread(daemon=True,target=mini()).start())
addtray.pack()

autoplay = tk.Button(canvas, fg= 'teal',bg='black',borderwidth=0,text = "Auto", command=auto_play)
autoplay.pack()


for root, dirs, files in os.walk(randompath):
    for pattern in pattern:
        for filename in fnmatch.filter(files, pattern):
            listBox.insert('end', filename)


def main():
    auto_play()
   # threading.Thread(daemon=True, target=mini).start()
   # canvas.protocol('WM_DELETE_WINDOW', mini)
    canvas.mainloop()

if __name__ == "__main__":
    main()
