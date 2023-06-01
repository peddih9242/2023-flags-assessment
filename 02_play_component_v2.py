# import modules
from tkinter import *
from functools import partial
import csv
import random

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

        root.withdraw()
        play = Play(send_to_play)


# play class, window where the user can play the quiz
class Play:

    def __init__(self, num_rounds):

        # set up play gui and font for gui
        self.play_box = Toplevel()

        # if users press cross at top, closes help and
        # 'releases' help button
        self.play_box.protocol("WM_DELETE_WINDOW", partial(self.close_play))

        gui_header = ("Microsoft PhagsPa", 16, "bold")
        button_font = ("Microsoft PhagsPa", 12, "normal")
        text_font = ("Microsoft PhagsPa", 10, "normal")

        self.play_frame = Frame(self.play_box)
        self.play_frame.grid(padx=10, pady=10)

        self.rounds_heading = Label(self.play_frame, text="Flag Quiz - Round # out of #",
                                    font=gui_header)
        self.rounds_heading.grid(row=0, padx=5, pady=5)

        quiz_instructions = "Try to answer the shown flag!"
        self.play_instructions = Label(self.play_frame, text=quiz_instructions,
                                       wraplength=275, justify="left", font=text_font)
        self.play_instructions.grid(row=1, padx=5, pady=5)

        self.rounds_frame = Frame(self.play_frame)
        self.rounds_frame.grid(row=2)

        # get properties of random flag and display it
        all_flags = self.get_all_flags()

        chosen_flag_list = self.random_flag(all_flags)
        chosen_directory = f"flag_images_resized/{chosen_flag_list[3]}"

        flag_image = PhotoImage(file=chosen_directory).subsample(5)

        self.image_display = Label(self.rounds_frame, image=flag_image)
        self.image_display.flag_image = flag_image
        self.image_display.grid(row=0, column=0, padx=10, pady=5)

        # make height of next_round button of similar height to flag image
        img_height = flag_image.height()
        next_rnd_height = img_height // 25

        self.next_round = Button(self.rounds_frame, text="Next Round",
                                 width=14, height=next_rnd_height, font=button_font,
                                 bg="#e1adff")
        self.next_round.grid(row=0, column=1, padx=5)

        self.choice_frame = Frame(self.play_frame, padx=10, pady=10)
        self.choice_frame.grid(row=3)

        for item in range(4):
            choice_button = Button(self.choice_frame, text=f"Choice {item + 1}",
                                   height=2, width=14, font=button_font, bg="#b8daff")

            choice_button.grid(row=item // 2,
                               column=item % 2,
                               padx=5, pady=5)

        result_label_text = "Question result will appear here"
        self.result_label = Label(self.play_frame, text=result_label_text,
                                  font=button_font, bg="#d4d4d4", width=30,
                                  highlightbackground="#c2c2c2",
                                  highlightthickness=2)
        self.result_label.grid(row=4, padx=5, pady=5)

        result_stat_text = "Correct - 0 \tIncorrect - 0"
        self.result_stat = Label(self.play_frame, text=result_stat_text,
                                 font=button_font, bg="#fff8bf", width=30,
                                 highlightbackground="#e0daa6",
                                 highlightthickness=2)
        self.result_stat.grid(row=5, padx=5, pady=5)

        # setup control frame and buttons
        self.control_frame = Frame(self.play_frame, padx=5, pady=5)
        self.control_frame.grid()

        control_button_details = [
            ["Help", "#f7dd8f", "get help"],
            ["Statistics", "#8c91ed", "get stats"],
            ["Start Over", "#d4d4d4", "start over"]
        ]

        for item in range(3):
            self.control_button = Button(self.control_frame, text=control_button_details[item][0],
                                         width=11, font=text_font,
                                         bg=control_button_details[item][1],
                                         command=lambda i=item: self.to_do(control_button_details[i][2]))
            self.control_button.grid(row=0, column=item, padx=5, pady=5)

    # function links buttons to designated function
    def to_do(self, request):

        if request == "get help":
            self.get_help()

        elif request == "get stats":
            self.get_stats()

        elif request == "start over":
            self.close_play()

    # function closes play window and shows rounds entry window
    def close_play(self):
        # reshow root (choose round) and destroy current box
        # to allow new game to start
        root.deiconify()
        self.play_box.destroy()

    # function to open help window when developed
    def get_help(self):
        print("You chose to get help")

    def get_stats(self):
        print("You chose to get stats")

    def get_all_flags(self):
        # open csv file and create reader
        csv_file = open("country_flags.csv")
        csv_reader = csv.reader(csv_file, delimiter=',')

        # set up list to hold colour data and skip first row (has headers)
        flag_data = []
        next(csv_reader)

        # add all colour data from csv file to list
        for item in csv_reader:
            flag_data.append(item)

        return flag_data

    def random_flag(self, flag_list):

        flag_index = random.randint(1, 198)
        chosen_flag_list = flag_list[flag_index]
        return chosen_flag_list


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    choose_rounds = ChooseRounds()
    root.mainloop()
