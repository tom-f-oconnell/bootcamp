
""" Introduction to Pandas """

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

df = pd.read_csv('../../data/wt_lac.csv', comment='#')
print(df['[IPTG] (mM)'])

# Read in data files with pandas
# without header=None, the first number will be interpreted as a column label
df_high = pd.read_csv('../../data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('../../data/xa_low_food.csv', comment='#', header=None)

df_low.columns = ['low']
df_high.columns = ['high']
df = pd.concat((df_low, df_high), axis=1)
df.to_csv('../../data/xa_food.csv', index=False)

df = pd.read_csv('../../data/xa_food.csv')
# drops the NaNs
df['high'].dropna()

# not 'tidy' because high / low food are represented by column membership, not a variable
df_tidy = pd.melt(df, var_name='food density', value_name='cross-sectional area (sq. micron)'\
    ).dropna()

print(df_tidy)

print(df_tidy.loc[(df_tidy['food density'] == 'low') & (df_tidy['cross-sectional area' + \
    ' (sq. micron)'] > 2100), :])


wc_dict = {'Klose': 16,
           'Fontaine': 13,
           'Klinsmann': 11,
           'Pele': 12,
           'Ronaldo': 15,
           'Muller': 14,
           'Koscis': 11
           }

nation_dict = {'Klose': 'Germany',
           'Fontaine': 'France',
           'Klinsmann': 'Germany',
           'Pele': 'Brazil',
           'Ronaldo': 'Brazil',
           'Muller': 'Germany',
           'Koscis': 'Hungary'
           }

s_nation = pd.Series(nation_dict)
s_goals = pd.Series(wc_dict)

df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})

print(df_wc.loc['Fontaine', :])
print(df_wc.loc[df_wc['nation'] == 'Germany', :])
