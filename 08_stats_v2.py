# import modules
from tkinter import *
from functools import partial
import random
import csv


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

        # set up gui
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
                                    font=("Microsoft PhagsPa", 16, "bold"))
        self.rounds_heading.grid(row=0, padx=5, pady=5)

        quiz_instructions = "Click the button with the name of the flag shown!"
        self.play_instructions = Label(self.play_frame, text=quiz_instructions,
                                       wraplength=275, justify="left")
        self.play_instructions.grid(row=1, padx=5, pady=5)

        self.all_results = []

        all_flags = self.get_all_flags()

        self.rounds_frame = Frame(self.play_frame)
        self.rounds_frame.grid(row=2)

        chosen_flag_info = self.random_flag(all_flags)

        chosen_flag_names = chosen_flag_info[0]
        chosen_flag_file = chosen_flag_info[1]

        # create link between the flag displayed and the correct name
        correct_flag_list = [chosen_flag_names[0], chosen_flag_file]

        chosen_directory = f"flag_images_resized/{chosen_flag_file}"

        # takes image and displays it
        flag_image = PhotoImage(file=chosen_directory).subsample(5)

        self.image_display = Label(self.rounds_frame, image=flag_image)
        self.image_display.flag_image = flag_image
        self.image_display.grid(row=0, column=0, padx=10, pady=5)

        # make height of next_round button of similar height to flag image
        img_height = flag_image.height()
        next_rnd_height = img_height // 25

        self.next_round = Button(self.rounds_frame, text="Next Round",
                                 width=14, height=next_rnd_height,
                                 bg="#e1adff", command=lambda: self.new_round(all_flags),
                                 state=DISABLED)
        self.next_round.grid(row=0, column=1, padx=5)

        self.choice_frame = Frame(self.play_frame, padx=10, pady=10)
        self.choice_frame.grid(row=3)

        random.shuffle(chosen_flag_names)

        self.choice_button_list = []

        for item in range(4):
            choice_button = Button(self.choice_frame, text=chosen_flag_names[item],
                                   height=2, width=14, bg="#b8daff", wraplength=100,
                                   command=lambda i=chosen_flag_names[item]: self.choice_compare(i, correct_flag_list))

            self.choice_button_list.append(choice_button)

            choice_button.grid(row=item // 2,
                               column=item % 2,
                               padx=5, pady=5)

        result_label_text = "Question result will appear here"
        self.result_label = Label(self.play_frame, text=result_label_text,
                                  bg="#d4d4d4", width=30,
                                  highlightbackground="#c2c2c2",
                                  highlightthickness=2, wraplength=200)
        self.result_label.grid(row=4, padx=5, pady=5)

        self.correct_rounds = 0
        self.incorrect_rounds = 0

        result_stat_text = f"Correct: {self.correct_rounds} \tIncorrect: {self.incorrect_rounds}"
        self.result_stat = Label(self.play_frame, text=result_stat_text,
                                 bg="#fff8bf", width=30,
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

        control_buttons = []

        for item in range(3):
            self.control_button = Button(self.control_frame, text=control_button_details[item][0],
                                         width=11, bg=control_button_details[item][1],
                                         command=lambda i=item: self.to_do(control_button_details[i][2]))
            self.control_button.grid(row=0, column=item, padx=5, pady=5)

            control_buttons.append(self.control_button)

        self.stats_button = control_buttons[1]
        self.stats_button.config(state=DISABLED)

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

    # function compares user choice with correct answer and updates gui
    def choice_compare(self, choice_name, correct_list):

        # enable next round button and stats button
        self.next_round.config(state=NORMAL)
        self.stats_button.config(state=NORMAL)

        # end game if the last game has been played (if infinite mode was not chosen)
        if self.current_round == self.num_rounds and self.num_rounds != "infinite":
            self.next_round.config(state=DISABLED)
            self.start_over.config(bg="#48bf15", text="Play Again", font=("Arial", 10, "bold"))

        # disable choice buttons
        for item in self.choice_button_list:
            item.config(state=DISABLED)

        correct_answer = correct_list[0]

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

        round_result = [choice_name, correct_answer]

        self.all_results.append(round_result)

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
        correct_incorrect = [self.correct_rounds, self.incorrect_rounds]
        self.stats_button.config(state=DISABLED)
        Stats(self, correct_incorrect, self.all_results)


class Stats:

    def __init__(self, partner, result_ratio, history):

        self.stats_box = Toplevel()
        self.stats_box.protocol("WM_DELETE_WINDOW", partial(self.close_stats,
                                                            partner))

        # create GUI

        self.stats_bg = "#a2d0fa"

        self.stats_frame = Frame(self.stats_box, padx=10, pady=10, bg=self.stats_bg)
        self.stats_frame.grid()

        self.stats_title = Label(self.stats_frame, text="Statistics / History",
                                 font=("Microsoft PhagsPa", "16", "bold"), bg=self.stats_bg)
        self.stats_title.grid(row=0, padx=5, pady=5)

        stats_instructions_text = "Welcome to the statistics window! Here you can see your correct rounds " \
                                  "and incorrect rounds with a percentage. You can also see your question history here, " \
                                  "using the arrow buttons to navigate through groups of five rounds."
        self.stats_instructions = Label(self.stats_frame, text=stats_instructions_text,
                                        wraplength=450, width=70, justify="left", bg=self.stats_bg,
                                        font=("Microsoft PhagsPa", "10", "normal"))
        self.stats_instructions.grid(row=1, padx=5, pady=5)

        total_correct = result_ratio[0]
        total_incorrect = result_ratio[1]

        # change colour of background of labels showing results
        if total_correct > total_incorrect:
            result_bg = "#84e37b"
        elif total_incorrect > total_correct:
            result_bg = "#ed8979"
        else:
            result_bg = "#fff8bf"

        self.total_results = Label(self.stats_frame, text=f"Correct: {total_correct} \t\tIncorrect: {total_incorrect}",
                                   width=70, bg=result_bg)
        self.total_results.grid(row=2, padx=5, pady=5)

        # calculate percentages of correct and incorrect rounds and display them
        percentage_correct = round((total_correct / (total_correct + total_incorrect)) * 100, 1)
        percentage_incorrect = round(100 - percentage_correct, 1)

        self.result_percentages = Label(self.stats_frame,
                                        text=f"Percentage Correct: {percentage_correct}% \t\tPercentage Incorrect: {percentage_incorrect}%",
                                        width=70, bg=result_bg)
        self.result_percentages.grid(row=3, padx=5, pady=5)
        
        self.history_start = 1
        self.history_end = 5
        
        if len(history) <= 5:
            shown_rounds_text = f"You are currently viewing rounds 1 to {len(history)}"
        else:
            shown_rounds_text = "You are currently viewing rounds 1 to 5"
        self.shown_rounds = Label(self.stats_frame, text=shown_rounds_text, width=70)
        self.shown_rounds.grid(row=4, padx=5, pady=5)

        # loop creates up to 5 separate labels showing individual rounds
        self.history_display_list = []

        if len(history) < 5:
            num_display = len(history)
        else:
            num_display = 5



        for item in range(num_display):

            # set background for each round shown based on if user is correct or not
            if history[item][0] == history[item][1]:
                display_bg = "#84e37b"
            else:
                display_bg = "#ed8979"
            
            self.display_history = Label(self.stats_frame, text=f"Round {item + 1} - Your answer: {history[item][0]}\t\tCorrect answer: {history[item][1]}",
                                         width=70, justify="left", wraplength=500, bg=display_bg)
            
            self.history_display_list.append(self.display_history)

            self.display_history.grid(row=5+item, padx=5)

        self.nav_frame = Frame(self.stats_frame, padx=5, pady=5, bg="#a2d0fa")
        self.nav_frame.grid(row=10)

        self.go_left = Button(self.nav_frame, text="<", state=DISABLED,
                              command=lambda: self.move_history(history, "left"))
        self.go_left.grid(row=0, column=0, padx=180)

        self.go_right = Button(self.nav_frame, text=">", command=lambda: self.move_history(history, "right"))
        self.go_right.grid(row=0, column=1, padx=180)

        # disable right arrow if not enough rounds played
        if len(history) <= 5:
            self.go_right.config(state=DISABLED)

        self.dismiss_stats = Button(self.stats_frame, text="Dismiss",
                                    width=25, bg="#60a0db", activebackground="#3b76ad",
                                    command=lambda: self.close_stats(partner),
                                    font=("Microsoft PhagsPa", 10, "normal"))
        self.dismiss_stats.grid(row=11, padx=5, pady=10)

    # function moves the viewed history further or back five rounds based on button pressed
    def move_history(self, history, direction):

        if direction == "right":

            self.history_start += 5
            self.history_end += 5

            disable_right = False

            # update labels displaying the history to show next 5 rounds
            count = self.history_start - 1
            for item in self.history_display_list:
                
                if count < len(history):

                    # set background for each round shown based on if user is correct or not
                    if history[count][0] == history[count][1]:
                        display_bg = "#84e37b"
                    else:
                        display_bg = "#ed8979"

                    item.config(text=f"Round {count + 1} - Your answer: {history[count][0]}\t\tCorrect answer: {history[count][1]}", bg=display_bg)

                else:
                    item.config(text="", bg=self.stats_bg)
                    disable_right = True

                count += 1

                if count == len(history):
                    disable_right = True

            self.go_left.config(state=NORMAL)

            if disable_right:
                self.go_right.config(state=DISABLED)

        else:

            self.history_start -= 5
            self.history_end -= 5

            disable_left = False

            # update labels displaying the history to show next 5 rounds
            count = self.history_start - 1
            for item in self.history_display_list:
                
                # set background for each round shown based on if user is correct or not
                if history[count][0] == history[count][1]:
                    display_bg = "#84e37b"
                else:
                    display_bg = "#ed8979"

                item.config(text=f"Round {count + 1} - Your answer: {history[count][0]}\t\tCorrect answer: {history[count][1]}", bg=display_bg)

                if self.history_start == 1:
                    disable_left = True

                count += 1

            self.go_right.config(state=NORMAL)

            if disable_left:
                self.go_left.config(state=DISABLED)

        # update the label showing user the rounds they're viewing
        if count > len(history):
            self.shown_rounds.config(text=f"You are currently viewing rounds {self.history_start} to {len(history)}")
        else:
            self.shown_rounds.config(text=f"You are currently viewing rounds {self.history_start} to {self.history_end}")


    # function closes the stats window and enables stats button
    def close_stats(self, partner):

        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    ChooseRounds()
    root.mainloop()
