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
    with open("../experiment_results/lr_mom_0_99.pkl", "rb") as f:
        model_dict = pickle.load(f)
except IOError:
    print("File not accessible")

lr_001 = np.array(model_dict.get("LR: 0.001, MOM: 0.99")).astype(float)
lr_005 = np.array(model_dict.get("LR: 0.005, MOM: 0.99")).astype(float)
lr_01 = np.array(model_dict.get("LR: 0.01, MOM: 0.99")).astype(float)
lr_015 = np.array(model_dict.get("LR: 0.015, MOM: 0.99")).astype(float)
lr_02 = np.array(model_dict.get("LR: 0.02, MOM: 0.99")).astype(float)


columns = [lr_001, lr_005, lr_01, lr_015, lr_02]

fig = plt.figure(figsize=(5, 3), dpi=80)

# Creating plot

plt.rcParams.update({'font.size': 18})
# Add title and axis names
plt.title('Learning rate & Momentum')
plt.xlabel('Models')
plt.ylabel('Test accuracy (%)')
B = plt.boxplot(columns)
plt.xticks([1, 2, 3, 4, 5], ['LR=0.001, MOM=0.99', 'LR=0.005, MOM=0.99', 'LR=0.01, MOM=0.99', 'LR=0.015, MOM=0.99', 'LR=0.02, MOM=0.99'], rotation='vertical')

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
