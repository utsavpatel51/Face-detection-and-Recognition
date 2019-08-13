from tkinter import Tk,messagebox
from tkinter import *
import numpy as np
import cv2
import requests,time

from dataset_genrator import dataset_gen
from face_recognizer import training
from face_detection import detection

root = Tk()
entrye1 = StringVar()
entrye2 = StringVar()
root.geometry("500x500")

def take_ip():
    global entrye1,entrye2
    _idx = entrye1.get()
    namex = entrye2.get()
    dataset_gen.genrate(_id=_idx,name=namex)
    messagebox.showinfo("Success","dataset capture")
def callback_db():
    t1 = Toplevel(root)
    Label(t1, text="ID").grid(row=0)
    Label(t1, text="Name").grid(row=1)
    e1 = Entry(t1,textvariable=entrye1)
    e2 = Entry(t1,textvariable=entrye2)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3 = Button(t1,text='submit',command=take_ip)
    e3.grid(row=2,column=1)
def callback_train():
    training.train()
    messagebox.showinfo("Success","training successful")
def callback_detect():
    detection.detect()
b = Button(root,text='genrate',command=callback_db)
b1 = Button(root,text='train',command=callback_train)
b2 = Button(root,text='detect',command=callback_detect)
b.place(x=100,y=250)
b1.place(x=200,y=250)
b2.place(x=300,y=250)
root.mainloop()