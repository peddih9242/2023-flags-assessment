# import modules
from tkinter import *


class ChooseRounds:

    def __init__(self):

        self.entry_frame = Frame(padx=10, pady=10)
        self.entry_frame.grid(row=3)

        self.rounds_entry = Entry(self.entry_frame, width=36)
        self.rounds_entry.grid(row=0, column=0, padx=5)

        self.infinite_button = Button(self.entry_frame, text="∞", width=4,
                                      bg="#e8cafc", activebackground="#d4afdb",
                                      command=lambda: self.to_play(True))
        self.infinite_button.grid(row=0, column=1, padx=5)

        self.confirm_button = Button(self.entry_frame, text="Confirm",
                                     width=15, bg="#d6d6d6", activebackground="#a1a1a1",
                                     command=lambda: self.to_play())
        self.confirm_button.grid(row=5, padx=5, pady=5)

    # function sends user to play window
    # -- make function when play class is being developed
    def to_play(self, infinite_mode=None):

        if infinite_mode:
            send_to_play = "infinite"
        else:
            var_num_rounds = self.rounds_entry.get()
            send_to_play = var_num_rounds
        Play(send_to_play)


# play class, window where the user can play the quiz
class Play:

    def __init__(self, num_rounds):

        self.play_box = Toplevel()

        self.play_frame = Frame(self.play_box)
        self.play_frame.grid()

        self.rounds_heading = Label(self.play_frame, text="Flag Quiz - Round # out of #",
                                    font=("Microsoft PhagsPa", 16, "bold"))
        self.rounds_heading.grid(row=0, padx=5, pady=5)

        quiz_instructions = "Play the game"
        self.play_instructions = Label(self.play_frame, text=quiz_instructions,
                                       wraplength=275, justify="left")
        self.play_instructions.grid(row=1, padx=5, pady=5)

        self.rounds_frame = Frame(self.play_frame)
        self.rounds_frame.grid(row=2)

        self.flag_image = Entry(self.rounds_frame, width=25)
        self.flag_image.grid(row=0, column=0)

        self.next_round = Button(self.rounds_frame, text="Next Round",
                                 width=12)
        self.next_round.grid(row=0, column=1)




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    ChooseRounds()
    root.mainloop()
