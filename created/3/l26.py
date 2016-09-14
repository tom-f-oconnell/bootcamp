
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

"""
# probably won't work. add to pythonpath
 import bootcamp_utils

rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Verify random number generator.

a = np.random.random(size=100000)
x, y = bootcamp_utils.ecdf(a)

# should be a straight line
plt.plot(x[::1000], y[::1000], marker='.', linestyle='none', markersize=10)
"""

# Generate 20 random numbers on uniform interval
x = np.random.random(size=20)

# Make them coin flips
heads = x > 0.5

# Show which were heads, and count the number of heads
print(heads)
print('\nThere were', np.sum(heads), ' heads.')

""" C. elegans example """

x = np.random.random(size=36)
reversals = x <= 9/36
print(np.sum(reversals))

""" Drawing normal data """

# Set parameters
mu = 10
sigma = 1

# Draw 10000 random samples
x = np.random.normal(mu, sigma, size=10000)

# Plot a histogram of our draws
_ = plt.hist(x, bins=100)
plt.show()

# Let's test the drawing by fitting the data
print(np.mean(x))
print(np.std(x))

# Key of bases
bases = 'ATGC'

# Draw random numbers for sequence
x = np.random.randint(0, 4, 50)

# Make sequence
seq_list = [None]*50
for i, b in enumerate(x):
    seq_list[i] = bases[b]

# Join the sequence
print(''.join(seq_list))

""" If you don't want replacement. """

# has replacement. problem.
np.random.randomint(0, 96, 20) 

# two solutions
np.random.choice(np.arange(96), size=20, replace=False)
np.random.permutation(np.arange(52))



