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
        self.rounds_entry.grid(row=0, column=0, padx=5)

        self.infinite_button = Button(self.entry_frame, text="∞", width=6,
                                      command=lambda: self.to_play())
        self.infinite_button.grid(row=0, column=1, padx=5)

        self.error_text = Label(self.start_frame, fg="#9e1e1e")

        self.confirm_button = Button(self.start_frame, text="Confirm",
                                     width=15, command=lambda: self.check_rounds())
        self.confirm_button.grid(row=5, padx=5, pady=5)

    # function checks if number of rounds is valid then
    # sends user to play window if rounds are valid
    def check_rounds(self):

        num_rounds = self.rounds_entry.get()
        has_error = False

        # try / except block checks for strings, then checks
        # inputted number is between 0 and 100
        try:
            num_rounds = int(num_rounds)
            if 0 < num_rounds < 100:
                self.to_play()
            else:
                if num_rounds <= 0:
                    error_info = "Number too low, enter above 0"
                elif num_rounds >= 100:
                    error_info = "Number too high, enter below 100"
                has_error = True

        except ValueError:
            error_info = "Please enter an integer between 0 and 100."
            has_error = True

        if has_error:
            # show error to user
            self.error_text.grid(row=4, padx=5)
            self.error_text.config(text=error_info)

    # function sends user to play window
    # -- make function when play class is being developed
    def to_play(self):
        pass


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    ChooseRounds()
    root.mainloop()
