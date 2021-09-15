
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("PDT to JST Clock") #Set the title of the window to PDT to JST Clock

#timezone = strftime("%z")
#print(timezone)

currentHour = int(strftime("%H")) + 16 #Takes PDT time and converts to JST
p = " AM"

#Makes the time within 24 hours
if currentHour > 24:
    currentHour = currentHour - 24

#Changes AM to PM if the hour is greater than 12
if currentHour > 12:
    p = " PM"
    currentHour = currentHour - 12

#Formats the way the time is displayed
def time():
    jstTime = str(currentHour) + ":" + strftime("%M:%S") + p
    timeLabel.config(text = jstTime)
    timeLabel.after(1000, time)

#Styles the text and the colors
timeLabel = Label(root, font = ("calibri", 40, "bold"),
                  background = "grey",
                  foreground = "white")

timeLabel.pack(anchor = "center")
time()

mainloop()