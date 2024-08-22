import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import time


root = tk.Tk()
flag = False
root.title("Timer")
root.geometry("400x700")
root.resizable(False, False)
root.config(bg="#000")

# create heading root
lbl_heading = tk.Label(
    root,
    text= "Timer",
    fg= "#BA0F30",
    bg="#000",
    font= "arial 30 bold",
)

# clock
lbl_clock = tk.Label(
    root,
    text= "",
    font= "arial 20",
    bg="#000",
    fg="#FAF7F4",
)

def set_clock():
    lbl_clock.config(text= time.strftime("Clock: %H:%M:%S %p", time.localtime()))
    lbl_clock.after(1000, set_clock)
set_clock()


# set timer
hour = tk.StringVar(value="00")
min = tk.StringVar(value="00")
sec = tk.StringVar(value="00")

image_set_5_m = tk.PhotoImage(file="image/5min.png").subsample(3, 3)
image_set_15_m = tk.PhotoImage(file="image/15min.png").subsample(3, 3)
image_set_20_m = tk.PhotoImage(file="image/20min.png").subsample(3, 3)
image_set_30_m = tk.PhotoImage(file="image/30min.png").subsample(3, 3)
image_set_45_m = tk.PhotoImage(file="image/45min.png").subsample(3, 3)
image_set_1_h = tk.PhotoImage(file="image/60min.png").subsample(3, 3)

def set_timer(number):
    if number == 60:
        hour.set(1)
        min.set(0)
    else:
        hour.set(0)
        min.set(number)
    sec.set(0)


btn_set_5_m = tk.Button(
    root,
    image= image_set_5_m,
    width=100,
    height=100,
    bg= "#000",
    activebackground= "#000",
    bd= 0,
    command= lambda: set_timer(5),
)

btn_set_15_m = tk.Button(
    root,
    image= image_set_15_m,
    width=100,
    height=100,
    bg= "#000",
    activebackground= "#000",
    bd= 0,
    command= lambda: set_timer(15),
)

btn_set_20_m = tk.Button(
    root,
    image= image_set_20_m,
    width=100,
    height=100,
    bg= "#000",
    activebackground= "#000",
    bd= 0,
    command= lambda: set_timer(20),
)

btn_set_30_m = tk.Button(
    root,
    image= image_set_30_m,
    width=100,
    height=100,
    bg= "#000",
    activebackground= "#000",
    bd= 0,
    command= lambda: set_timer(30),
)

btn_set_45_m = tk.Button(
    root,
    image= image_set_45_m,
    width=100,
    height=100,
    bg= "#000",
    activebackground="#000",
    bd= 0,
    command= lambda: set_timer(45),
)
btn_set_1_h = tk.Button(
    root,
    image= image_set_1_h,
    width=100,
    height=100,
    bg= "#000",
    activebackground= "#000",
    bd= 0,
    command= lambda: set_timer(60),
)

def check_set_timer():
    try:
        if int(hour.get()) != 0 or int(min.get()) != 0 or int(sec.get()) != 0:
            btn_start["state"] = "normal"
            btn_reset["state"] = "normal"
        else:
            btn_reset["state"] = "disabled"
            btn_start["state"] = "disabled"
    except ValueError:
        messagebox.showerror(title="Error", message="You must enter a number to set the timer.")
        reset_timer()
    finally:
        root.after(500, check_set_timer)

list_of_ent = [hour, min, sec]
for num, ent in enumerate(list_of_ent):
    tk.Entry(
    root,
    textvariable= ent,
    bg= "#000",
    fg= "#FAF7F4",
    bd= 0,
    width= 2,
    font= "arial 50",
    ).place(x=(40 * (num * 3 + 1)), y=160)

lbl_heading_timer = tk.Label(
    root,
    text= "Hour   \t\t   Min     \t\t     Sec",
    bg= "#000",
    fg= "#FAF7F4",
    font= "arial 10 bold",
)


def set_hour():
    h = int(hour.get()) 
    assert h >= 0 and h <= 99, "Select hour from 00 to 99."
    return h

def set_min():
    m = int(min.get()) 
    assert m >= 0 and m <= 59, "Select min from 00 to 59."
    return m
    
def set_sec():
    s = int(sec.get()) 
    assert s >= 0 and s <= 59, "Select sec from 01 to 59."
    return s


# set button state disabled function
def btn_disabled(string):
    """string : Literal["active", "disabled"]"""

    btn_set_5_m["state"] = string
    btn_set_15_m["state"] = string
    btn_set_20_m["state"] = string
    btn_set_30_m["state"] = string
    btn_set_45_m["state"] = string
    btn_set_1_h["state"] = string
    btn_start["state"] = string

#  reset timer
def reset_timer():
    btn_reset["state"] = "active"
    hour.set("00")
    min.set("00")
    sec.set("00")


# start timer
def start_timer():
    btn_disabled("disabled")
    try:
        hours = set_hour()
        minutes = set_min()
        second = set_sec()
    except ValueError:
        messagebox.showerror(title="Error", message="You must enter a number to set the timer.")
    except AssertionError as err:
        messagebox.showerror(title="Error", message=err)
    else:
        while (hours != 0 or minutes != 0 or second != 0):
            if minutes == 0 and second == 0:
                hours -= 1
                minutes = 59
                second = 59
            elif second == 0:
                minutes -= 1
                second = 59
            else:
                second -= 1
            hour.set(hours)
            min.set(minutes)
            sec.set(second)
            if btn_reset["state"] != "active":
                root.update()
                time.sleep(1)
        if btn_reset["state"] != "active": 
            playsound("music/mixkit-clock-bells-hour-signal-1069.wav")
    finally:
        hour.set("00")
        min.set("00")
        sec.set("00")
        btn_disabled("active")
        


btn_start = tk.Button(
    root,
    text= "START",
    font= "arial 20",
    bg= "#009",
    fg= "#FAF7F4",
    activebackground= "#009",
    bd= 0,
    command= start_timer,
    default="disabled",
)

btn_reset = tk.Button(
    root,
    text= "RESET",
    font= "arial 20",
    bg= "#FF2511",
    fg= "#FAF7F4",
    activebackground= "#FF2511",
    bd= 0,
    command= reset_timer,
    default="disabled",
)

check_set_timer()


lbl_heading.place(x=140, y=10)
lbl_clock.place(x=70, y=70)
lbl_heading_timer.place(x=60, y=140)
btn_start.place(x=70, y=600)
btn_reset.place(x=220, y=600)
btn_set_5_m.place(x=25, y=300)
btn_set_15_m.place(x=145, y=300)
btn_set_20_m.place(x=265, y=300)
btn_set_30_m.place(x=25 , y=450)
btn_set_45_m.place(x=145, y=450)
btn_set_1_h.place(x=265, y=450)
root.mainloop()