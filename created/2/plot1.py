
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set matplotlib rc file
# don't need to do this every time
# rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
# sns.set(rc=rc)

# load food data
high = np.loadtxt('../../data/xa_high_food.csv')
low = np.loadtxt('../../data/xa_low_food.csv')

# TODO do this with fewer min and max commands
lomin = np.min(low)
lomax = np.max(low)
highmin = np.min(high)
highmax = np.max(high)
allmin = np.min([lomin, highmin])
allmax = np.max([lomax, highmax])

bins = np.arange(allmin-50, allmax+50, 50)


# plot the data as a histogram in shitty MATLAB style
_ = plt.hist((low,high), bins=bins, normed=True, histtype='stepfilled', alpha=0.5)

# can bake fontsize=18 into matplotlib defaults
# in matplotlib rc params (see above)

plt.xlabel('Cross-sectional area (um$^2$)')
plt.ylabel('Frequency', rotation='horizontal')
plt.legend(('Low concentration', 'High concentration'), loc='upper right')
plt.show()

# save the figure
plt.savefig('egg_area_histogram.svg', bbox_inches='tight')
