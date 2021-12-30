import tkinter
from tkinter import *
import sys
import os
import pickle

win=tkinter.Tk()
win.title('Snake Game')
win.geometry('200x200')
bg=PhotoImage(file="menuback.png")
label1 =Label(win,image=bg)
label1.place(x=0,y=0)
def run():
    os.system('python snakegamepygame.py')
def exit():
    sys.exit()
btn=Button(win,text='PLAY',bd='10',bg='black',fg='white',relief=FLAT,command=run)
btn2=Button(win,text='EXIT',bd='12',bg='black',fg='white',relief=FLAT,command=exit)
btn.pack(pady=30)
btn2.pack(pady=20)

label2=Label(win,text='High Score:')
with open('score.dat','rb') as file:
  var=StringVar()
  var=pickle.load(file)
  label3=Label(win,text='High Score:'+str(var),relief=FLAT)
  label3.pack()
win.mainloop()