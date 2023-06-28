# import modules
from tkinter import *
from functools import partial


# play class, window where the user can play the quiz
class Play:

    def __init__(self):

        # setup control frame and buttons
        self.control_frame = Frame(padx=5, pady=5)
        self.control_frame.grid()

        control_button_details = [
            ["Help", "#f7dd8f", "get help"],
            ["Statistics", "#8c91ed", "get stats"],
            ["Start Over", "#d4d4d4", "start over"]
        ]

        control_buttons = []

        for item in range(3):
            self.control_button = Button(self.control_frame, text=control_button_details[item][0],
                                         width=11,
                                         bg=control_button_details[item][1],
                                         command=lambda i=item: self.to_do(control_button_details[i][2]))
            self.control_button.grid(row=0, column=item, padx=5, pady=5)

            control_buttons.append(self.control_button)

        self.help_button = control_buttons[0]
        self.start_over = control_buttons[2]

    # function links buttons to designated function
    def to_do(self, request):

        if request == "get help":
            self.get_help()

        elif request == "get stats":
            self.get_stats()

        elif request == "start over":
            self.close_play()

    # function to open help window
    def get_help(self):
        self.help_button.config(state=DISABLED)
        Help(self)

    def get_stats(self):
        print("You chose to get stats")

    def close_play(self):
        print("You chose to start over")


class Help:

    def __init__(self, partner):

        self.help_box = Toplevel()
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help,
                                                           partner))

        # create GUI
        self.help_frame = Frame(self.help_box, padx=10, pady=10, bg="#ffe387")
        self.help_frame.grid()

        self.help_title = Label(self.help_frame, text="Help",
                                font=("Microsoft PhagsPa", "16", "bold"), bg="#ffe387")
        self.help_title.grid(row=0, padx=5, pady=5)

        instructions_text = "Welcome to the help window! Currently you should have chosen the number of rounds, which you will play " \
                            "that number of rounds.\n\nWhen you're playing the game you will be shown a flag that represents a country. " \
                            "To win you must choose (by clicking) the button which has the name of the country that the flag represents. " \
                            "After choosing which country you think the flag is from you will be able to play more rounds (if there are more rounds to be played)" \
                            "by clicking the 'next round button', which will bring you to the next round." \
                            "You will also be able to check your current game history by clicking on the 'Statistics' button at the bottom of the" \
                            "play window\n\n" \
                            "Want to play more after? Click the 'start over' (or 'play again button if you have completed your game') or the X at the top right of the window " \
                            "to go back to choose the number of rounds you want to play, and start again from the beginning!"

        self.instructions = Label(self.help_frame, text=instructions_text,
                                  wraplength=330, width=50, justify="left", bg="#ffe387",
                                  font=("Microsoft PhagsPa", "10", "normal"))
        self.instructions.grid(row=1)

        self.dismiss_help = Button(self.help_frame, text="Dismiss",
                                   width=15, bg="#e0af46", activebackground="#f0c362",
                                   command=lambda: self.close_help(partner),
                                   font=("Microsoft PhagsPa", 10, "normal"))
        self.dismiss_help.grid(row=2, padx=5, pady=10)

    # function sends user to play window
    def close_help(self, partner):

        # reshow root and destroy current box
        root.deiconify()
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    Play()
    root.mainloop()
