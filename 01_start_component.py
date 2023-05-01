# import modules
from tkinter import *


class ChooseRounds:

    def __init__(self):

        # create GUI
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.flags_title = Label(self.start_frame, text="Flags Quiz",
                                 font=("Arial", "16", "bold"))
        self.flags_title.grid(row=0, padx=5, pady=5)

        round_instructions_text = "Enter the number of rounds you would like to play, " \
                                  "or click the button with the infinity symbol for infinite mode."
        self.round_instructions = Label(self.start_frame, text=round_instructions_text,
                                        wraplength=300, width=40, justify="left")
        self.round_instructions.grid(row=1)

        self.entry_frame = Frame(self.start_frame, padx=10, pady=10)
        self.entry_frame.grid(row=3)

        self.rounds_entry = Entry(self.entry_frame, width=34)
        self.rounds_entry.grid(row=0, column=0, padx=5, pady=5)

        self.infinite_button = Button(self.entry_frame, text="∞", width=6)
        self.infinite_button.grid(row=0, column=1, padx=5)

        self.error_text = Label(self.start_frame, text="")

        self.confirm_button = Button(self.start_frame, text="Confirm",
                                     width=15)
        self.confirm_button.grid(row=5, padx=5)

    # function checks if number of rounds is valid then
    # sends user to play window if rounds are valid
    def check_rounds(self):

        num_rounds = self.rounds_entry.get()
        if 0 < num_rounds < 100:
            self.to_play()
        else:
            if num_rounds < 0:
                error_info = "Number too low, enter above 0"
            elif num_rounds > 100:
                error_info = "Number too low, enter below 100"
                # handling text?

            # show error to user
            self.error_text.grid()
            self.error_text.config()

    def to_play(self):
        pass

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    ChooseRounds()
    root.mainloop()
