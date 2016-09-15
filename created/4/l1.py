
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

df = pd.read_csv('../../data/frog_tongue_adhesion.csv', comment='#')

df = df.rename(columns={'impact force (mN)': 'impf'})

gb_frog = df.groupby('ID')
mean_impf = gb_frog['impf'].mean()
sem_impf = gb_frog['impf'].sem()

# don't use
sns.barplot(data=df, x='ID', y='impf')

plt.figure()
sns.boxplot(data=df, x='ID', y='impf')

plt.figure()
# keep an eye on "AltAir" or something like that. another plotting library.
# sns.swarmplot(data=df, x='ID', y='impf')

# could also consider overlaying this over box plot
sns.swarmplot(data=df, x='ID', y='impf', hue='date')
plt.show()
plt.gca().legend_.remove()

