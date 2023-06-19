import csv
import random

# function returns a random flag from flag list
def random_flag(flag_list):
    # get the flag that will be the correct flag this round
    correct_flag_list = random.choice(flag_list)

    correct_flag_file = correct_flag_list[3]

    chosen_flag_lists = []
    choice_flag_names = [correct_flag_list[0]]

    count = 1

    while count < 4:

        chosen_flag = random.choice(flag_list)
        if chosen_flag in chosen_flag_lists:
            continue
        chosen_flag_lists.append(chosen_flag)
        count += 1

    for item in chosen_flag_lists:
        choice_flag_names.append(item[0])

    return [choice_flag_names, correct_flag_file]


def get_all_flags():
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


# main routine
all_flags = get_all_flags()
limited_flags = []
for item in range(4):
    limited_flags.append(all_flags[item])

print(limited_flags)
random_flags = random_flag(limited_flags)
print(random_flags)
