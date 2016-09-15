
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../../data/frog_tongue_adhesion.csv', comment='#')

df_big_force = df.loc[df['impact force (mN)'] > 1000, :]
print(df_big_force)

# a simple experiment, because tidy gaurantees
print(df.loc[42,:])

# df.loc[:, 'impact force (mN)'] is more or less equivalent to df['impact force (mN)']
print(df.loc[:, ['impact force (mN)', 'adhesive force (mN)']])

plt.plot(df['impact force (mN)'], df['adhesive force (mN)'], marker='.', linestyle='none')
plt.show()

"""
plt.figure()
plt.plot(df.loc[:,'total contact area (mm2)'], df.loc[:,'adhesive force (mN)'], marker='.', \
    linestyle='none')
plt.show()
"""

df.plot(x='total contact area (mm2)',y='adhesive force (mN)', kind='scatter')

# for all pairwise correlations
print(df.corr())

# to slice this
print(df.loc[:, ['impact force (mN)', 'adhesive force (mN)']].corr())

# returns a new dataframe with the rename. not mutable by default.
df.rename(columns={'impact force (mN)': 'impf'})

# would need to do this
df = df.rename(columns={'impact force (mN)': 'impf'})

# df['impf'] equivalent to df.impf
# only works without special characters
