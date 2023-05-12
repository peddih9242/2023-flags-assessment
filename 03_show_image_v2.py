# Import tkinter library
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame
win = Tk()

# Set the geometry
win.geometry("800x400")

# Load the image
img = Image.open("nzflag.png")

# Convert To photoimage
tkimage = ImageTk.PhotoImage(img)

# Display the Image
label = Label(win, image=tkimage)
label.pack()
win.mainloop()
