import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('experiment_results.pkl')

axes = df.groupby(df.columns//10, axis=1).boxplot(subplots=True, figsize=(12, 18))

plt.xlabel('Time (s)')
plt.ylabel('ms')
plt.show()