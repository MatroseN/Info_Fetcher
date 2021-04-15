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
batch_size_64 = np.array(model_dict.get("Batch_size: 64")).astype(float)
batch_size_128 = np.array(model_dict.get("Batch_size: 128")).astype(float)


columns = [batch_size_8, batch_size_16, batch_size_32, batch_size_64, batch_size_128]

fig = plt.figure(figsize=(10, 7))

# Creating plot
# Add title and axis names
plt.title('Batch size')
plt.xlabel('Models')
plt.ylabel('Test accuracy %')
plt.boxplot(columns)
plt.xticks([1, 2, 3, 4, 5], ['Batch_size:8', 'Batch_size:16', 'Batch_size:32', 'Batch_size:64', 'Batch_size:128'])

# show plot
plt.show()
