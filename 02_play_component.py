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
        play = Play(send_to_play)


# play class, window where the user can play the quiz
class Play:

    def __init__(self, num_rounds):

        # set up play gui and font for gui
        self.play_box = Toplevel()
        gui_header = ("Microsoft PhagsPa", 16, "bold")
        gui_font = ("Microsoft PhagsPa", 12, "normal")

        self.play_frame = Frame(self.play_box)
        self.play_frame.grid(padx=10, pady=10)

        self.rounds_heading = Label(self.play_frame, text="Flag Quiz - Round # out of #",
                                    font=gui_header)
        self.rounds_heading.grid(row=0, padx=5, pady=5)

        quiz_instructions = "Play the game"
        self.play_instructions = Label(self.play_frame, text=quiz_instructions,
                                       wraplength=275, justify="left", font=gui_font)
        self.play_instructions.grid(row=1, padx=5, pady=5)

        self.rounds_frame = Frame(self.play_frame)
        self.rounds_frame.grid(row=2)

        # takes image and displays it
        flag_image = PhotoImage(file="flag_images_resized/WS-flag.gif").subsample(5)

        self.image_display = Label(self.rounds_frame, image=flag_image)
        self.image_display.flag_image = flag_image
        self.image_display.grid(row=0, column=0)

        self.next_round = Button(self.rounds_frame, text="Next Round",
                                 width=12, height=3, font=gui_font)
        self.next_round.grid(row=0, column=1, padx=5)

        self.choice_frame = Frame(self.play_frame, padx=10, pady=10)
        self.choice_frame.grid(row=3)

        for item in range(4):
            choice_button = Button(self.choice_frame, text=f"Choice {item + 1}",
                                   height=2, width=14, font=gui_font)

            choice_button.grid(row=item // 2,
                               column=item % 2,
                               padx=5, pady=5)

        result_label_text = "Question result will appear here"
        self.result_label = Label(self.play_frame, text=result_label_text,
                                  font=gui_font, bg="#d4d4d4", width=30,
                                  highlightbackground="#c2c2c2",
                                  highlightthickness=2)
        self.result_label.grid(row=4, padx=5, pady=5)

        result_stat_text = "Correct - 0 \tIncorrect - 0"
        self.result_stat = Label(self.play_frame, text=result_stat_text,
                                 font=gui_font, bg="#fff8bf", width=30,
                                 highlightbackground="#e0daa6",
                                 highlightthickness=2)
        self.result_stat.grid(row=5, padx=5, pady=5)

        # setup control frame and buttons
        self.control_frame = Frame(self.play_frame, padx=5, pady=5)
        self.control_frame.grid()

        control_button_details = ["Help", "Statistics", "Start Over"]

        for item in range(3):
            self.control_button = Button(self.control_frame, text=control_button_details[item],
                                         width=11, font=("Microsoft PhagsPa", 10, "normal"))
            self.control_button.grid(row=0, column=item, padx=5, pady=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    choose_rounds = ChooseRounds()
    root.mainloop()
