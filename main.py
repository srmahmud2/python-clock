from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("clock")

# define a function to get our time


# create label to store clock
label = Label(root, font=("dis-digital", 80), background='black', foreground="Cyan")
# now lets pack our label
label.pack(anchor="center")


def time():
    string = strftime('%H:%M:%S %p')
    # set the time to the label
    label.config(text=string)
    label.after(1000, time)
# outside the time() function lets call the time function


time()

mainloop()
