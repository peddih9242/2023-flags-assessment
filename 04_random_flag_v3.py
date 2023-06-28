from tkinter import *
import csv
import random


# play class, window where the user can play the quiz
class Play:

    def __init__(self):

        # set up gui
        self.play_frame = Frame()
        self.play_frame.grid(padx=10, pady=10)

        all_flags = self.get_all_flags()

        self.rounds_frame = Frame(self.play_frame)
        self.rounds_frame.grid(row=2)
    
        self.duplicate_files = [""]
        self.current_round = 1

        chosen_flag_info = self.random_flag(all_flags)

        chosen_flag_names = chosen_flag_info[0]
        chosen_flag_file = chosen_flag_info[1]

        random.shuffle(chosen_flag_names)

        chosen_directory = f"flag_images_resized/{chosen_flag_file}"

        # takes image and displays it
        flag_image = PhotoImage(file=chosen_directory).subsample(5)

        self.image_display = Label(self.play_frame, image=flag_image)
        self.image_display.flag_image = flag_image
        self.image_display.grid(row=0, column=0, padx=10, pady=5)

        # make height of next_round button of similar height to flag image
        img_height = flag_image.height()
        next_rnd_height = img_height // 25

        self.next_round = Button(self.rounds_frame, text="Next Round",
                                 width=14, height=next_rnd_height,
                                 bg="#e1adff", command=lambda: self.new_round(all_flags))
        self.next_round.grid(row=0, column=1, padx=5)

        self.choice_frame = Frame(self.play_frame, padx=10, pady=10)
        self.choice_frame.grid(row=1)

        random.shuffle(chosen_flag_names)

        self.choice_button_list = []

        for item in range(4):
            choice_button = Button(self.choice_frame, text=chosen_flag_names[item],
                                   height=2, width=14, bg="#b8daff", wraplength=100)

            self.choice_button_list.append(choice_button)

            choice_button.grid(row=item // 2,
                               column=item % 2,
                               padx=5, pady=5)

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

        flag_list = flag_list[:4]

        # get the flag that will be the correct flag this round
        # and make sure the file will not be the same two rounds in a row
        while True:
            correct_flag_list = random.choice(flag_list)

            correct_flag_file = correct_flag_list[3]
            if correct_flag_file in self.duplicate_files:
                continue
            else:
                self.duplicate_files.pop(0)
                self.duplicate_files.append(correct_flag_file)
                break

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

        print(choice_flag_names)
        print(correct_flag_file)

        return [choice_flag_names, correct_flag_file]
    
    def new_round(self, flag_list):

        self.current_round += 1

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
                        command=lambda i=chosen_flag_names[choice_config_count]: self.choice_compare(i, correct_flag_list))

            choice_config_count += 1


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    play = Play()
    root.mainloop()
