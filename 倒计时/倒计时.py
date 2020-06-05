#!/usr/bin/env python
# coding=utf-8

import threading
import time
import queue
from tkinter import *
import tkinter.messagebox
import logging

logging.basicConfig(level=logging.INFO)

## Communication queue
commQueue = queue.Queue()
g_time = 0


## Function run in thread
def timeThread():
    global g_time
    g_time = timeVar.get() * 60
    while 1:
        logging.info("线程放入队列:%d".decode("utf-8") % g_time)
    commQueue.put(g_time)
    try:
        root.event_generate('<<TimeChanged>>', when='tail')
    except TclError:
        pass
    time.sleep(1)
    g_time -= 1
    if g_time == -1:
        begin_btn["fg"] = "black"
        clockVar.set("开始计时")
        pass


def timeChanged(event):
    x = commQueue.get()
    logging.info("获取队列:%d".decode("utf-8") % x)
    minits = x // 60
    seconds = x % 60
    s = "剩余时间 {:02}:{:02}".format(minits, seconds)
    begin_btn["fg"] = "blue"
    clockVar.set(s)
    if x == 0:
        tkMessageBox.showinfo("提醒", "时间已到")


def clock_func(*args):
    global g_time
    if threading.activeCount() > 1:
        g_time = timeVar.get() * 60
    else:
        th = threading.Thread(target=timeThread)
    th.start()


## Create main window
root = Tk()
root.title("计时工具")
root.geometry("180x95-0-45")
root.resizable(width=FALSE, height=FALSE)
root.wm_attributes("-topmost", 1)
frame = Frame(root)
frame.pack()
Label(frame, text="设定时间间隔").grid(row=1, column=2)
timeVar = IntVar()
clockVar = StringVar()
time_entry = Entry(frame, textvariable=timeVar, width=8)
time_entry["justify"] = "center"
time_entry.grid(row=2, column=2, sticky="W,E")
begin_btn = Button(frame, textvariable=clockVar, command=clock_func)
begin_btn.grid(row=3, column=2)
timeVar.set(8)
begin_btn["fg"] = "black"
clockVar.set("开始计时")

for child in frame.winfo_children():
    child.grid_configure(pady=3)

time_entry.focus()
root.bind('<<TimeChanged>>', timeChanged)
root.bind("<Return>", clock_func)
root.mainloop()