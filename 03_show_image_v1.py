# import modules
from tkinter import *


class ChooseRounds:

    def __init__(self, image):

        self.entry_frame = Frame(padx=10, pady=10)
        self.entry_frame.grid()

        self.display_image = Label(self.entry_frame, image=image)
        self.display_image.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    var_image = PhotoImage(file="AE-flag.gif")
    choose_rounds = ChooseRounds(var_image)
    root.mainloop()
