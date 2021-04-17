# import required module
import os
import re
import csv
import pickle
import pprint

model_dict = {}

try:
    with open("../experiment_results/lr_mom.pkl", "rb") as f:
        model_dict = pickle.load(f)
except IOError:
    print("File not accessible")

accuracy_list = []

# This will be the key in the dictionary for this models entry
model_label = "LR: 0.02, MOM: 0"

# setting flag and index to 0
count = 0

# assign directory
directory = '../LR Momentum/Custom_logs'

search_string = "(numpy=0.015>,).*?(numpy=0>}).*?"

pattern = re.compile(search_string)

folder = ""


def get_full_path(specific_file):
    # Iterate over files in directory
    for r, di, fi in os.walk(directory):
        for name in fi:
            if name == specific_file:
                return os.path.join(r, name)


def accuracy_fetcher(folder, accuracy_list):
    path = folder + "_prediction.csv"
    full_file_path = get_full_path(path)
    print(full_file_path)
    reader = csv.DictReader(open(full_file_path))
    for data in map(dict, reader):
        accuracy = data.get("num_correct_percent")
        accuracy_list.append(accuracy)
    return accuracy_list


# Read text File
def read_text_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        # Loop through the file line by line
        for line in f:
            # checking string is present in line or not
            for match in re.finditer(pattern, line):
                return True


# Iterate over files in directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith("hyper.csv") or filename.endswith("model_settings.json"):
            file_path = os.path.join(root, filename)
            # if a regex match in a text file occurs find that models test accuracy and add it as a list to
            # model_dict as a new entry
            if read_text_file(file_path):
                dir_path = os.path.dirname(os.path.realpath(file_path))
                dir_path = os.path.basename(os.path.normpath(dir_path))
                print()
                print(dir_path)
                acc = accuracy_fetcher(dir_path, accuracy_list)
                model_dict[model_label] = acc

                f = open("../experiment_results/lr_mom.pkl", "wb")
                pickle.dump(model_dict, f)
                f.close()

pprint.pprint(model_dict)
