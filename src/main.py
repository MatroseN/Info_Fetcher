# import required module
import os
import re

# assign directory
directory = '../Batch/Custom_logs/'

search_string = "^.*batch_size,8.*$"

pattern = re.compile(search_string)

# setting flag and index to 0
count = 0


# Read text File
def read_text_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        # Loop through the file line by line
        for line in f:
            # checking string is present in line or not
            for match in re.finditer(pattern, line):
                print("found")
                return True


# Iterate over files in directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith("hyper.csv") or filename.endswith("model_settings.json"):
            file_path = os.path.join(root, filename)
            if read_text_file(file_path):
                count += 1

print()
print("Matches:")
print(count)
