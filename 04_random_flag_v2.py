from tkinter import *
import csv
import random


# play class, window where the user can play the quiz
class Play:

    def __init__(self):

        # set up
        self.play_frame = Frame()
        self.play_frame.grid(padx=10, pady=10)

        all_flags = self.get_all_flags()

        chosen_flag_info = self.random_flag(all_flags)

        chosen_flag_names = chosen_flag_info[0]
        chosen_flag_file = chosen_flag_info[1]

        # add link for names and files
        chosen_flag_file.append(0)

        for item in range(1, 4):
            chosen_flag_names.append(item)

        chosen_directory = f"flag_images_resized/{chosen_flag_file}"

        # takes image and displays it
        flag_image = PhotoImage(file=chosen_directory).subsample(5)

        self.image_display = Label(self.play_frame, image=flag_image)
        self.image_display.flag_image = flag_image
        self.image_display.grid(row=0, column=0, padx=10, pady=5)

        self.choice_frame = Frame(self.play_frame, padx=10, pady=10)
        self.choice_frame.grid(row=1)

        random.shuffle(chosen_flag_names)

        for item in range(4):
            choice_button = Button(self.choice_frame, text=chosen_flag_names[item],
                                   height=2, width=14, bg="#b8daff", wraplength=100)

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

        # get the flag that will be the correct flag this round
        correct_flag_index = random.randint(1, 197)

        correct_flag_list = flag_list[correct_flag_index]
        correct_flag_file = correct_flag_list[3]

        choice_flag_index = []

        choice_flag_names = [correct_flag_list[0]]

        count = 1

        while count < 4:

            flag_index = random.randint(1, 198)
            if flag_index in choice_flag_index or flag_index == correct_flag_index:
                continue
            choice_flag_index.append(flag_index)
            count += 1

        for item in choice_flag_index:
            choice_flag_names.append(flag_list[item][0])

        print(choice_flag_names)
        print(correct_flag_file)

        return [choice_flag_names, correct_flag_file]


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    play = Play()
    root.mainloop()
