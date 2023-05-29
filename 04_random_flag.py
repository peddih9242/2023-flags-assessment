import csv
import random


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


def random_flag(flag_list):

    flag_index = random.randint(1, 198)
    chosen_flag_list = flag_list[flag_index]
    print(chosen_flag_list)


# main routine
all_flags = get_all_flags()

# output all colour data from list
for flag in all_flags:
    print(flag)

print()

random_flag(all_flags)