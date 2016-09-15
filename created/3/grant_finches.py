
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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



