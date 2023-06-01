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

        chosen_flag_list = self.random_flag(all_flags)
        chosen_directory = f"flag_images_resized/{chosen_flag_list[3]}"
        print(chosen_flag_list)

        # takes image and displays it
        flag_image = PhotoImage(file=chosen_directory).subsample(5)

        self.image_display = Label(self.play_frame, image=flag_image)
        self.image_display.flag_image = flag_image
        self.image_display.grid(row=0, column=0, padx=10, pady=5)

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
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Flags Quiz")
    play = Play()
    root.mainloop()