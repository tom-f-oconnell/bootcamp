
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cv(x):
    """ Coefficient of variation: variance divided by absolute value of the mean """
    return np.var(x) / abs(np.mean(x))

df = pd.read_csv('../../data/frog_tongue_adhesion.csv', comment='#')

""" Practice using df.loc """

# Pa = newton per square meter (a derived unit of pressure)
adh_over_2000 = df.loc[(df['adhesive strength (Pa)'] < -2000) | (df['adhesive strength (Pa)'] \
    > 2000)]
imp_and_adh_frog2 = df.loc[df['ID'] == 'II', ['impact force (mN)', 'adhesive force (mN)']]
adh_and_time_3a4 = df.loc[(df['ID'] == 'III') | (df['ID'] == 'IV'), ['adhesive force (mN)', \
    'time frog pulls on target (ms)']]

""" Practice with groupby() """

# but first, the long way
nums = ['I','II','III','IV']

mean_impacts = []
for i in range(len(nums)):
    mean_impacts.append(df.loc[df['ID'] == nums[i], 'impact force (mN)'].mean())

# TODO solution? faster way to get to a numpy array?
print(np.array(mean_impacts))

# We only want ID's and impact forces, so slice those out
df_impf = df.loc[:, ['ID', 'impact force (mN)']]

# Make a GroupBy object
grouped = df_impf.groupby('ID')
print(grouped)

# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)

# Look at the new DataFrame
print(df_mean_impf)

print(df_mean_impf.loc['III', :])

results = grouped.agg([np.mean, np.median, np.std, cv])

print(df.loc[:, ['ID','impact force (mN)', 'adhesive force (mN)']].groupby('ID').agg(\
    [np.mean, np.median, np.std, cv]))


