# import modules
from tkinter import *
from functools import partial
import csv
import random


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

        self.current_round = 1

        # initiate round variable for rounds heading
        if num_rounds == "infinite":
            self.num_rounds = "infinite"
            heading_text = "Infinite Mode"

        else:
            self.num_rounds = int(num_rounds)
            heading_text = f"Round {self.current_round} out of {self.num_rounds}"

        self.rounds_heading = Label(self.play_frame, text=f"Flag Quiz - {heading_text}",
                                    font=gui_header, justify="center")
        self.rounds_heading.grid(row=0, padx=5, pady=5)

        quiz_instructions = "Click the button with the name of the flag shown!"
        self.play_instructions = Label(self.play_frame, text=quiz_instructions,
                                       wraplength=275, justify="left", font=text_font)
        self.play_instructions.grid(row=1, padx=5, pady=5)

        self.rounds_frame = Frame(self.play_frame)
        self.rounds_frame.grid(row=2)

        all_flags = self.get_all_flags()

        chosen_flag_info = self.random_flag(all_flags)

        chosen_flag_names = chosen_flag_info[0]
        chosen_flag_file = chosen_flag_info[1]

        # create link between the flag displayed and the correct name
        correct_flag_list = [chosen_flag_names[0], chosen_flag_file]

        chosen_directory = f"flag_images_resized/{chosen_flag_file}"

        flag_image = PhotoImage(file=chosen_directory).subsample(5)

        self.image_display = Label(self.rounds_frame, image=flag_image)
        self.image_display.flag_image = flag_image
        self.image_display.grid(row=0, column=0, padx=10, pady=5)

        # make height of next_round button of similar height to flag image
        img_height = flag_image.height()
        next_rnd_height = img_height // 25

        self.next_round = Button(self.rounds_frame, text="Next Round",
                                 width=14, height=next_rnd_height, font=button_font,
                                 bg="#e1adff", command=lambda: self.new_round(all_flags),
                                 state=DISABLED)
        self.next_round.grid(row=0, column=1, padx=5)

        self.choice_frame = Frame(self.play_frame, padx=10, pady=10)
        self.choice_frame.grid(row=3)

        # randomise choice names for random button positions
        random.shuffle(chosen_flag_names)

        self.choice_button_list = []

        for item in range(4):
            choice_button = Button(self.choice_frame, text=chosen_flag_names[item],
                                   height=3, width=14, font=button_font, bg="#b8daff",
                                   wraplength=100,
                                   command=lambda i=chosen_flag_names[item]: self.choice_compare(i, correct_flag_list))

            self.choice_button_list.append(choice_button)

            choice_button.grid(row=item // 2,
                               column=item % 2,
                               padx=5, pady=5)

        result_label_text = "Question result will appear here"
        self.result_label = Label(self.play_frame, text=result_label_text,
                                  font=button_font, bg="#d4d4d4", width=30,
                                  highlightbackground="#c2c2c2",
                                  highlightthickness=2, wraplength=200)
        self.result_label.grid(row=4, padx=5, pady=5)

        self.correct_rounds = 0
        self.incorrect_rounds = 0

        result_stat_text = f"Correct: {self.correct_rounds} \tIncorrect: {self.incorrect_rounds}"
        self.result_stat = Label(self.play_frame, text=result_stat_text,
                                 font=button_font, bg="#fff8bf", width=30,
                                 highlightbackground="#e0daa6",
                                 highlightthickness=2, wraplength=200)
        self.result_stat.grid(row=5, padx=5, pady=5)

        # setup control frame and buttons
        self.control_frame = Frame(self.play_frame, padx=5, pady=5)
        self.control_frame.grid()

        control_button_details = [
            ["Help", "#f7dd8f", "get help"],
            ["Statistics", "#8c91ed", "get stats"],
            ["Start Over", "#d4d4d4", "start over"]
        ]

        control_buttons = []

        for item in range(3):
            self.control_button = Button(self.control_frame, text=control_button_details[item][0],
                                         width=11, font=text_font,
                                         bg=control_button_details[item][1],
                                         command=lambda i=item: self.to_do(control_button_details[i][2]))
            self.control_button.grid(row=0, column=item, padx=5, pady=5)

            control_buttons.append(self.control_button)

        self.start_over = control_buttons[2]

    # function returns list of all flag data
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

    # function returns a random flag from flag list
    def random_flag(self, flag_list):
        # get the flag that will be the correct flag this round
        correct_flag_list = random.choice(flag_list)

        correct_flag_file = correct_flag_list[3]

        chosen_flag_lists = []
        choice_flag_names = [correct_flag_list[0]]

        count = 1

        while count < 4:

            chosen_flag = random.choice(flag_list)
            if chosen_flag in chosen_flag_lists or chosen_flag == correct_flag_list:
                continue
            chosen_flag_lists.append(chosen_flag)
            count += 1

        for item in chosen_flag_lists:
            choice_flag_names.append(item[0])

        return [choice_flag_names, correct_flag_file]

    def choice_compare(self, choice_name, correct_list):

        # enable next round button
        self.next_round.config(state=NORMAL)

        # end game if the last game has been played (if infinite mode was not chosen)
        if self.current_round == self.num_rounds and self.num_rounds != "infinite":
            self.next_round.config(state=DISABLED)
            self.start_over.config(bg="#48bf15", text="Play Again", font=("Arial", 10, "bold"))

        # disable choice buttons
        for item in self.choice_button_list:
            item.config(state=DISABLED)

        correct_answer = correct_list[0]

        # update result label, choice buttons and correct / incorrect rounds based on result
        if choice_name in correct_list:
            self.result_label.config(text=f"Correct! The answer was {correct_answer}.",
                                     bg="#84e37b", highlightbackground="#3cb031")
            self.correct_rounds += 1

        else:
            self.result_label.config(text=f"Incorrect! The answer was {correct_answer}.",
                                     bg="#ed8979", highlightbackground="#c9432e")
            self.incorrect_rounds += 1

        self.result_stat.config(text=f"Correct: {self.correct_rounds} \tIncorrect: {self.incorrect_rounds}")

        if self.correct_rounds > self.incorrect_rounds:
            self.result_stat.config(bg="#84e37b", highlightbackground="#3cb031")

        elif self.incorrect_rounds > self.correct_rounds:
            self.result_stat.config(bg="#ed8979", highlightbackground="#c9432e")

        else:
            self.result_stat.config(bg="#fff8bf", highlightbackground="#e0daa6")

    def new_round(self, flag_list):

        # update rounds heading and question result text and styling
        self.current_round += 1
        if self.num_rounds == "infinite":
            self.rounds_heading.config(text=f"Flag Quiz - Round {self.current_round}")
        else:
            self.rounds_heading.config(text=f"Flag Quiz - Round {self.current_round} out of {self.num_rounds}")
        self.result_label.config(bg="#d4d4d4", highlightbackground="#c2c2c2",
                                 text="Question result will appear here")

        # re-enable choice buttons and disable next round button
        for item in self.choice_button_list:
            item.config(state=NORMAL)

        self.next_round.config(state=DISABLED)

        chosen_flag_info = self.random_flag(flag_list)

        chosen_flag_names = chosen_flag_info[0]
        chosen_flag_file = chosen_flag_info[1]

        # create link between the flag displayed and the correct name
        correct_flag_list = [chosen_flag_names[0], chosen_flag_file]

        chosen_directory = f"flag_images_resized/{chosen_flag_file}"

        # takes image and displays it
        flag_image = PhotoImage(file=chosen_directory).subsample(5)

        self.image_display.config(image=flag_image)
        self.image_display.flag_image = flag_image

        # make height of next_round button of similar height to flag image
        img_height = flag_image.height()
        next_rnd_height = img_height // 25

        self.next_round.config(height=next_rnd_height)

        random.shuffle(chosen_flag_names)

        choice_config_count = 0
        for item in self.choice_button_list:
            item.config(text=chosen_flag_names[choice_config_count],
                        command=lambda i=chosen_flag_names[choice_config_count]: self.choice_compare(i,
                                                                                                     correct_flag_list))

            choice_config_count += 1

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    choose_rounds = ChooseRounds()
    root.mainloop()
