# import required module
import os
import re
import csv

# assign directory
directory = '../Batch/Custom_logs/'

search_string = "^.*batch_size,8.*$"

pattern = re.compile(search_string)

folder = ""

# setting flag and index to 0
count = 0

# assign directory
directory = '../Batch/Custom_logs/'

search_string = "^.*batch_size,8.*$"

pattern = re.compile(search_string)

folder = ""

# setting flag and index to 0
count = 0


def get_full_path(specific_file):
    # Iterate over files in directory
    for r, di, fi in os.walk(directory):
        for name in fi:
            if name == specific_file:
                return os.path.join(r, name)


def accuracy_fetcher(folder):
    path = folder + "_prediction.csv"
    accuracy = None
    full_file_path = get_full_path(path)

    reader = csv.DictReader(open(full_file_path))
    for data in map(dict, reader):
        accuracy = data.get("num_correct_percent")
    print()
    print("Accuracy:")
    print(accuracy)


# Read text File
def read_text_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        # Loop through the file line by line
        for line in f:
            # checking string is present in line or not
            for match in re.finditer(pattern, line):
                print()
                print("////////////////--------------//////////////////")
                print("Value: " + match.string + " found in file")
                print(file_path)
                return True


# Iterate over files in directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith("hyper.csv") or filename.endswith("model_settings.json"):
            file_path = os.path.join(root, filename)
            if read_text_file(file_path):
                dir_path = os.path.dirname(os.path.realpath(file_path))
                dir_path = os.path.basename(os.path.normpath(dir_path))
                accuracy_fetcher(dir_path)
                count += 1

print()
print("Matches:")
print(count)
