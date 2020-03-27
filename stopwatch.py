from tkinter import *
from  datetime import datetime
temp = 0
after_id = ''

def sec():
    global temp, after_id
    after_id = display.after(1000, sec)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    display.configure(text = str(f_temp))
    temp += 1

def sw_start():
    button_start.grid_forget()
    button_stop.grid(row = 1, columnspan = 2, sticky = "ew")
    sec()

def sw_stop():
    button_stop.grid_forget()
    button_continue.grid(row = 1, column = 0, sticky = "ew")
    button_restart.grid(row = 1, column = 1, sticky = "ew")
    display.after_cancel(after_id)

def sw_continue():
    button_restart.grid_forget()
    button_continue.grid_forget()
    button_stop.grid(row=1, columnspan=2, sticky="ew")
    sec()

def sw_restart():
    global temp
    temp = 0
    display.configure(text = "00:00")
    button_restart.grid_forget()
    button_continue.grid_forget()
    button_start.grid(row=1, columnspan=2, sticky="ew")

root = Tk()
root.title("Stopwatch")
display = Label(root, width = 5, font =("Atomic" , 100), text = "00:00")
display.grid(row = 0, columnspan = 2)
button_start = Button(root, text = "Start", font = ("Atomic", 30), command = sw_start)
button_stop = Button(root, text = "Stop", font = ("Atomic", 30), command = sw_stop)
button_continue = Button(root, text = "Continue", font = ("Atomic", 30), command = sw_continue)
button_restart = Button(root, text = "Restart", font = ("Atomic", 30), command = sw_restart)

button_start.grid(row = 1, columnspan = 2, sticky = "ew")
root.mainloop()