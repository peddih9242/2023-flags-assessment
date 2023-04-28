# import modules
from tkinter import *


class ChooseRounds:

    def __init__(self):

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.flags_title = Label(self.start_frame, text="Flags Quiz")
        self.flags_title.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    ChooseRounds()
    root.mainloop()