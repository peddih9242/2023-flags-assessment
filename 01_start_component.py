# import modules
from tkinter import *


class ChooseRounds:

    def __init__(self):

        # create GUI
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.flags_title = Label(self.start_frame, text="Flags Quiz",
                                 font=("Microsoft PhagsPa", "16", "bold"))
        self.flags_title.grid(row=0, padx=5, pady=5)

        round_instructions_text = "Enter the number of rounds you would like to play, " \
                                  "or click the button with the infinity symbol for infinite mode."
        self.round_instructions = Label(self.start_frame, text=round_instructions_text,
                                        wraplength=275, width=40, justify="left",
                                        font=("Microsoft PhagsPa", "10", "normal"))
        self.round_instructions.grid(row=1)

        self.entry_frame = Frame(self.start_frame, padx=10, pady=10)
        self.entry_frame.grid(row=3)

        self.rounds_entry = Entry(self.entry_frame, width=36)
        self.rounds_entry.grid(row=0, column=0, padx=5)

        self.infinite_button = Button(self.entry_frame, text="∞", width=4,
                                      bg="#e8cafc", activebackground="#d4afdb",
                                      command=lambda: self.to_play(True))
        self.infinite_button.grid(row=0, column=1, padx=5)

        self.rounds_feedback = Label(self.start_frame)

        self.confirm_button = Button(self.start_frame, text="Confirm",
                                     width=15, bg="#d6d6d6", activebackground="#a1a1a1",
                                     command=lambda: self.check_rounds(),
                                     font=("Microsoft PhagsPa", 10, "normal"))
        self.confirm_button.grid(row=5, padx=5, pady=5)

    # function checks if number of rounds is valid then
    # sends user to play window if rounds are valid
    def check_rounds(self):

        num_rounds = self.rounds_entry.get()
        has_error = False

        # try / except makes sure that input is an integer from 1 to 99
        try:
            num_rounds = int(num_rounds)
            if 0 < num_rounds < 100:
                self.to_play()
            else:
                has_error = True

        except ValueError:

            has_error = True

        self.rounds_feedback.grid(row=4, padx=5)

        # if an error is found in rounds chosen, show an error in the error_text label
        if has_error:

            error_info = "Please enter an integer between 0 and 100."
            self.rounds_feedback.config(text=error_info, fg="#9e1e1e")

        elif not has_error:
            self.rounds_feedback.config(text="You are OK", fg="#30a608")

    # function sends user to play window
    # -- make function when play class is being developed
    def to_play(self, infinite_mode=None):

        if infinite_mode:
            self.rounds_feedback.grid(row=4, padx=5)
            self.rounds_feedback.config(text="Infinite mode chosen!", fg="#a62da6")
        else:
            self.rounds_entry.get()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    ChooseRounds()
    root.mainloop()
