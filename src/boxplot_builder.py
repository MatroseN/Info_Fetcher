# import required module
import os
import re
import csv
import pickle
import pprint
# Import libraries
import matplotlib.pyplot as plt
import numpy as np

model_dict = {}

try:
    with open("experiment_results.pkl", "rb") as f:
        model_dict = pickle.load(f)
except IOError:
    print("File not accessible")


batch_size_8 = np.array(model_dict.get("Batch_size: 8")).astype(float)
batch_size_16 = np.array(model_dict.get("Batch_size: 16")).astype(float)
batch_size_32 = np.array(model_dict.get("Batch_size: 32")).astype(float)


columns = [batch_size_8, batch_size_16, batch_size_32]

fig = plt.figure(figsize=(10, 7))

# Creating plot
plt.boxplot(columns)

# show plot
plt.show()
