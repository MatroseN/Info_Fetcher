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
    with open("../experiment_results/activation_functions.pkl", "rb") as f:
        model_dict = pickle.load(f)
except IOError:
    print("File not accessible")

LReLU_1 = np.array(model_dict.get("Leaky_ReLU: Alpha(0.1)")).astype(float)
LReLU_2 = np.array(model_dict.get("Leaky_ReLU: Alpha(0.2)")).astype(float)
LReLU_3 = np.array(model_dict.get("Leaky_ReLU: Alpha(0.3)")).astype(float)
LReLU_4 = np.array(model_dict.get("Leaky_ReLU: Alpha(0.4)")).astype(float)
LReLU_5 = np.array(model_dict.get("Leaky_ReLU: Alpha(0.5)")).astype(float)

Sigmoid = np.array(model_dict.get("Sigmoid")).astype(float)

Hard_Sigmoid = np.array(model_dict.get("Hard_Sigmoid")).astype(float)

TanH = np.array(model_dict.get("TanH")).astype(float)

columns = [LReLU_1, LReLU_2, LReLU_3, LReLU_4, LReLU_5, Sigmoid, Hard_Sigmoid, TanH]

fig = plt.figure(figsize=(5, 3), dpi=80)

# Creating plot
plt.rcParams.update({'font.size': 18})
# Add title and axis names
plt.title('Activation functions')
plt.xlabel('Models')
plt.ylabel('Test accuracy (%)')
B = plt.boxplot(columns)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ['LReLU alpha(0.1)', 'LReLU alpha(0.2)', 'LReLU alpha(0.3)', 'LReLU alpha(0.4)', 'LReLU alpha(0.5)', 'Sigmoid', 'Hard_Sigmoid', 'TanH'], rotation='vertical')

for k, v in model_dict.items():
    v = [float(item) for item in v]

    v = np.array(v)
    v = np.round(v, 4)

    print()
    print(k)

    min_accuracy = round(min(v), 4)
    max_accuracy = round(max(v), 4)
    median = round(np.median(v), 4)
    upper_quartile = round(np.percentile(v, 75), 4)
    lower_quartile = round(np.percentile(v, 25), 4)

    iqr = upper_quartile - lower_quartile
    upper_whisker = round(v[v <= upper_quartile + 1.5 * iqr].max(), 4)
    lower_whisker = round(v[v >= lower_quartile - 1.5 * iqr].min(), 4)

    lower_quartile = str(lower_quartile)
    lower_whisker = str(lower_whisker)
    median = str(median)
    upper_quartile = str(upper_quartile)
    upper_whisker = str(upper_whisker)
    data = [lower_whisker, lower_quartile, median, upper_quartile, upper_whisker]
    print("Lower Whisker:")
    print(lower_whisker)
    print("Lower Quartile:")
    print(lower_quartile)
    print("Median:")
    print(median)
    print("Upper Quartile:")
    print(upper_quartile)
    print("Upper Whisker:")
    print(upper_whisker)
    print("Min:")
    print(min_accuracy)
    print("Max:")
    print(max_accuracy)

# show plot
plt.show()
