
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import stats

finch_1973 = pd.read_csv('../../data/grant_1973.csv', comment='#')
finch_1975 = pd.read_csv('../../data/grant_1975.csv', comment='#')
finch_1987 = pd.read_csv('../../data/grant_1987.csv', comment='#')
finch_1991 = pd.read_csv('../../data/grant_1991.csv', comment='#')
finch_2012 = pd.read_csv('../../data/grant_2012.csv', comment='#')

#finch_1973['year'] = np.ones(len(finch_1973)) * 1973
finch_1975['year'] = np.ones(len(finch_1975)) * 1975
finch_1987['year'] = np.ones(len(finch_1987)) * 1987
finch_1991['year'] = np.ones(len(finch_1991)) * 1991
finch_2012['year'] = np.ones(len(finch_2012)) * 2012

std_name = {'Beak length, mm': 'beak length (mm)', 'Beak depth, mm': 'beak depth (mm)', \
            'yearband': 'year', 'blength': 'beak length (mm)', 'beak depth': 'beak depth (mm)'\
            ,'beak length': 'beak length (mm)', 'bdepth': 'beak depth (mm)'}
finch_1973 = finch_1973.rename(columns=std_name)
finch_1975 = finch_1975.rename(columns=std_name)
finch_1987 = finch_1987.rename(columns=std_name)
finch_1991 = finch_1991.rename(columns=std_name)
finch_2012 = finch_2012.rename(columns=std_name)

df = pd.concat((finch_1973, finch_1975, finch_1987, finch_1991, finch_2012), axis=0)

# remove duplicates within the same year (TODO check this against Justin's complete file)
df.drop_duplicates(subset={'year','band'}, inplace=True)

# can compare to finch_complete
# finch_complete = pd.read_csv('../../data/grant_complete.csv', comment='#')

# save the file. can maybe diff to compare if same file is gauranteed with these params
df.to_csv('../../my_grant_complete.csv', index=False)

""" 4.1 data analysis """

fortis = df.loc[(df['species'] == 'fortis') & (df['year'] == 1987)]
scandens = df.loc[(df['species'] == 'scandens') & (df['year'] == 1987)]

"""
print(fortis['beak depth (mm)'])
print(fortis['beak length (mm)'])
print(scandens['beak depth (mm)'])
print(scandens['beak length (mm)'])
"""

fortis_depth, fortis_d_cpx = stats.ecdf(fortis['beak depth (mm)'])
scandens_depth, scandens_d_cpx = stats.ecdf(scandens['beak depth (mm)'])

fortis_length, fortis_d_cpx = stats.ecdf(fortis['beak length (mm)'])
scandens_length, scandens_d_cpx = stats.ecdf(scandens['beak length (mm)'])

plt.plot(fortis_depth, fortis_d_cpx, marker='.', linestyle='none')
plt.plot(scandens_depth, scandens_d_cpx, marker='.', linestyle='none')
plt.title('Distribution of beak depths in 1987')
plt.ylabel('ECDF')
plt.xlabel('Beak depth (mm)')
plt.legend(('Fortis', 'Scandens'))
plt.margins(0.02)

plt.figure()
plt.plot(fortis_length, fortis_d_cpx, marker='.', linestyle='none')
plt.plot(scandens_length, scandens_d_cpx, marker='.', linestyle='none')
plt.title('Distribution of beak lengths in 1987')
plt.ylabel('ECDF')
plt.xlabel('Beak length (mm)')
plt.legend(('Fortis', 'Scandens'))
plt.margins(0.02)

plt.figure()
plt.plot(fortis_length, fortis_depth, marker='.', linestyle='none', color='b')
plt.plot(scandens_length, scandens_depth, marker='.', linestyle='none', color='r')
plt.title('Distribution of beak lengths in 1987')
plt.ylabel('Beak depth (mm)')
plt.xlabel('Beak length (mm)')
plt.legend(('Fortis', 'Scandens'))
plt.margins(0.02)

plt.show()
