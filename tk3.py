#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
import os, sys

def clicked():
    global lb1, lb2, click_count,clickvar
    click_count = click_count+1
    clickvar.set(click_count)
    print("CLick Me!")
    lb1.configure(text=f"label:{click_count}")

def gui():
    global lb1,lb2, click_count, clickvar
    click_count=0
    root = tk.Tk()
    clickvar=tk.IntVar(0)
    
    
    frame1 = ttk.Frame(root)
    lb1=ttk.Label(frame1,text='Label1')
    lb2=ttk.Label(frame1,text='Label2', textvariable=clickvar)
    bt1=ttk.Button(root,text="Exit",command=sys.exit)
    bt2=ttk.Button(root,text='Click ME!',command=clicked)
    
    lb1.pack(side="left",padx=3,pady=3)
    lb2.pack(side="left",padx=3,pady=3)
    frame1.pack(side="top",padx=3,pady=3)
    bt2.pack(side="top",padx=3,pady=3)
    bt1.pack(side="top",padx=3,pady=3)
    # implementation
    # ...
    root.mainloop()
def onExitButton():
    # implementation
    pass
def main(args):
    gui()    
if '__main__' == __name__:
    main(sys.argv)
