
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("JST Clock") #Set the title of the window to JST Clock

#Get the UTC offset of the local time and split it into a list to separate the hour difference
timeUTC = strftime("%z")
timeUTC = list(timeUTC)

#Get the hour difference from the UTC offset
if len(timeUTC) > 4:
    timeUTCHour = timeUTC[1] + timeUTC[2]
else:
    timeUTCHour = timeUTC[0] + timeUTC[1]

currentHour = int(strftime("%H")) + int(timeUTCHour) #Converts local time to UTC time

jstTime = currentHour + 9 #Convert UTC time to JST time
p = " AM"

#Makes the time within 24 hours
if jstTime > 24:
    jstTime = jstTime - 24
print(jstTime)

#Changes AM to PM if the hour is greater than 12
if jstTime >= 12:
    p = " PM"
    jstTime = jstTime - 12

#Formats the way the time is displayed
def time():
    finalTime = str(jstTime) + ":" + strftime("%M:%S") + p
    timeLabel.config(text = finalTime)
    timeLabel.after(1000, time)

#Styles the text and the colors
timeLabel = Label(root, font = ("calibri", 40, "bold"),
                  background = "grey",
                  foreground = "white")

timeLabel.pack(anchor = "center")
time()

mainloop()