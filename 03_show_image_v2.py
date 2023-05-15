# import modules
from tkinter import *


class ChooseRounds:

    def __init__(self):

        self.image = PhotoImage(file="AE-flag.gif").subsample(5)

        self.entry_frame = Frame(padx=10, pady=10)
        self.entry_frame.grid()

        self.display_image = Label(self.entry_frame, image=self.image)
        self.display_image.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    choose_rounds = ChooseRounds()
    root.mainloop()
