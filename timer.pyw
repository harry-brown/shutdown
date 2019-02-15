# !/usr/bin/python3
import os
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("200x150")

L1 = Label(top, text = "Hours: ")
L1.pack(side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

def startTimerFunc():
   try:
      os.system('shutdown.exe -s -t ' + str(int(float(E1.get())*60*60)))
   except:
      msg = messagebox.showinfo( "Error", "Error converting value to minutes")
      
def abortTimerFunc():
   os.system('shutdown.exe -a')

startButton = Button(top, text = "Start Timer", command = startTimerFunc)
startButton.place(x = 10,y = 10)
abortButton = Button(top, text = "Abort Timer", command = abortTimerFunc)
abortButton.place(x = 100,y = 10)
top.mainloop()
