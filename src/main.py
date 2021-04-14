# import required module
import os

# assign directory
directory = 'TestDir'


# Read text File
def read_text_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        print(f.read())


# Iterate over files in directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        file_path = os.path.join(root, filename)
        read_text_file(file_path)
