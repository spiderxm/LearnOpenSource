import os
import pygame
import time
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


sngs_lst = []
i = 0
p = 1
now = 0
# ------------------------------------------------


def directory_chooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            sngs_lst.append(files)
            print(files)
    print(sngs_lst)
    pygame.mixer.init()
    pygame.mixer.music.load(sngs_lst[0])
    pygame.mixer.music.play()


def next(event):
    global i
    if i == len(sngs_lst)-1:
        i = 0
    else:
        i += 1

    pygame.mixer.music.load(sngs_lst[i])
    pygame.mixer.music.play()
    Updatesong()


def prev(event):
    global i
    if i == 0:
        i = len(sngs_lst)-1
    else:
        i -= 1

    pygame.mixer.music.load(sngs_lst[i])
    pygame.mixer.music.play()
    Updatesong()


def stop(event):
    global p
    if p == 0:
        p = 1
    else:
        p = 0
    if p == 0:
        pygame.mixer.music.load(sngs_lst[i])
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()
        pygame.mixer.init()


def Updatesong():
    global i
    v.set(sngs_lst[i])


def up(event):
    global now
    now = 0
    now += pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(now + 0.1)


def down(event):
    global now
    now = 0
    now += pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(now - 0.1)


def rewind(event):
    pygame.mixer.music.rewind()
    Updatesong()


def DONE(event):
    print(v1.get())
    input  = v1.get()
    options = webdriver.ChromeOptions()
    options.set_headless()
    driver = webdriver.Chrome("C:/Users/Prakhar Pratyush/Desktop/ChromeDriver/chromedriver.exe",chrome_options=options)
    driver.get("http://genius.com")
    driver.find_element_by_name("q").click()
    print("Search Box Clicked...")

    try:
        element_present = EC.presence_of_element_located((By.NAME, "q"))
        WebDriverWait(driver, 20).until(element_present)
        driver.find_element_by_name("q").send_keys(input + Keys.ENTER)
        print("input send")

    except TimeoutError:
        print("failed to load page")

    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, "mini_card-info"))
        WebDriverWait(driver, 20).until(element_present)
        driver.find_element_by_class_name("mini_card-info").click()
        print("clicked")
    except TimeoutError:
        print("failed to open lyrics page")

    try:
        time.sleep(15)
        output = driver.find_element(By.XPATH, "/html/body/routable-page/ng-outlet/song-page/div/div/div[2]/div[1]/div/defer-compile[1]/lyrics/div/div/section/p")
        print(output)
        print(output.text)
        global t
        t = str(output.text)
        lyrics_print()
    except TimeoutError:
        print("failed to open lyrics page")


def lyrics_print():
    Lyrics.delete(1.0,END)
    Lyrics.insert('1.0', t)
    E1.delete(0,END)

# ----------------------------------------------
root = Tk()

wbcolor = "#252228"
wfcolor = "#fff"
label = Label(root, text ="Music Player",font=("Anton",35,"bold"),foreground=wfcolor,background=wbcolor)#<-----------------------
label.pack(fill=BOTH,expand=1)

frame = Frame(root)
frame.pack(fill=BOTH,expand=1)

bottomframe = Frame(root,background=wbcolor)  #<------------------
bottomframe.pack(side=BOTTOM,fill=BOTH,expand=1)

listbox = Listbox(frame, bd=8, width=30, height=24,font=("Oswald", 12),background="black",foreground="white") #<------------------
listbox.pack(side=LEFT, fill=BOTH,expand=1)

directory_chooser()

sngs_lst.reverse() # To insert song list in proper sequence
print(sngs_lst)

for s in sngs_lst:
    listbox.insert(0, s)  # here  we have inbuilt insert method so we can use it directly

sngs_lst.reverse()  # Getting back to the original sequence as the rest operations code are according to original list

v = StringVar()
v.set(sngs_lst[0])
songlabel = Label(root, textvariable= v, width= 60,font=("Arial",20),pady=25,background=wbcolor,foreground="#588A2D") #<-------------------
songlabel.pack(fill=BOTH,expand=1)

frame1 = Frame(root,background=wbcolor,pady=5)
frame1.pack(fill=BOTH,expand=1)

# Taking input of song name for lyrics:
T1= Label(frame1,text="Enter Song Name :",bd=0,font=("Arial", 12),background=wbcolor,foreground=wfcolor) #<------------------------
T1.pack(side=LEFT,padx=20)
v1= StringVar()
v1.set("Playing Now...")
E1 = Entry(frame1,textvariable=v1,bd=1,background="#DEDEDE",foreground="black") #<---------------------------
E1.pack(side=LEFT)

bcolor = "#B3C9B3"
fcolor = "black"
donebtn = Button(frame1,text="Download Lyrics",bd=0,background=bcolor,foreground=fcolor,cursor="target")
donebtn.pack(side=LEFT,padx=20)
donebtn.bind("<Button-1>",DONE)

Lyrics = Text(frame, bd=8, width=30,font=("Oswald",10),padx=3,pady=3,background="black",foreground="white") #<---------------------
Lyrics.pack(side=RIGHT,fill=BOTH,expand=1)
# -----------------------------------------------------------------------------------------------------------------------------------
rwndbtn = Button(bottomframe,text="Rewind",width=10,background=bcolor,bd=0,foreground=fcolor,cursor="target")
rwndbtn.pack(side=LEFT,padx=20)
rwndbtn.bind("<Button-1>", rewind)

prvbtn = Button(bottomframe, text="Previous Song",width=13,bd=0,background=bcolor,foreground=fcolor,cursor="target")
prvbtn.pack(side=LEFT,padx=250)
prvbtn.bind("<Button-1>", prev)

stopbtn = Button(bottomframe, text="Play/Pause",width=13,bd=0,background=bcolor,foreground=fcolor,cursor="target")
stopbtn.pack(side=LEFT)
stopbtn.bind("<Button-1>", stop)

voldwn = Button(bottomframe,text="Volume_down",bd=0,background=bcolor,foreground=fcolor,cursor="target")
voldwn.pack(side=RIGHT,padx=15)
voldwn.bind("<Button-1>", down)

volup = Button(bottomframe, text="Volume_up",width=12,bd=0,background=bcolor,foreground=fcolor,cursor="target")
volup.pack(side=RIGHT,padx=5)
volup.bind("<Button-1>", up)

nxtbtn = Button(bottomframe, text="Next Song",width=13,bd=0,background=bcolor,foreground=fcolor,cursor="target")
nxtbtn.pack(side=RIGHT,padx=190)
# No inbuilt method for button to select next so we will create a new method
nxtbtn.bind("<Button-1>", next)


# -----------------------------------------------------------------------------------------------------------------------------------
root.mainloop()
