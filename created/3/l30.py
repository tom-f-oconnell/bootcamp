
""" Introduction to Pandas """

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Read in data files with pandas
# without header=None, the first number will be interpreted as a column label
df_high = pd.read_csv('../../data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('../../data/xa_low_food.csv', comment='#', header=None)


