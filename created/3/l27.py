
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

def bs_resample(data, iters=100000, f=np.mean):
   """ Bootstrap resamples mean iters times and returns an array of that length. """
   bs_reps = np.empty(iters)

    # Compute replicates
   for i in range(iters):
       bs_sample = np.random.choice(data, size=len(bd_1975))
       """ Could do a replicate of any statistic we wanted:
       CV, std, artibtrary percentiles, whatever, but here we are doing a 
       bootstrap estimate of the mean.
       """
       bs_reps[i] = f(bs_sample)

   return bs_reps

bd_1975 = np.loadtxt('../../data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('../../data/beak_depth_scandens_2012.csv')

# Compute ECDFs for 1975 and 2012
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

# Plot the ECDFs
plt.plot(x_1975, y_1975, marker='.', linestyle='none')
plt.plot(x_2012, y_2012, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('1975', '2012'), loc='lower right')
plt.show()

print(np.mean(bd_1975))
print(np.mean(bd_2012))

bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))

# Compute ECDF of bootstrap sample
x_bs, y_bs = ecdf(bs_sample)

plt.figure()
# Plot the ECDFs
plt.plot(x_1975, y_1975, marker='.', linestyle='none')
plt.plot(x_bs, y_bs, marker='.', linestyle='none', alpha=0.5)
plt.margins(0.02)
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('1975', 'bootstrap'), loc='lower right')
plt.show()

"""
Confidence interval = if we were to repeat experiment many times, interval in which sample
parameter values value with given confidence.

Key is to not make statements about true parameter value (frequentist statistics CAN'T
attempt to assign probabilities relative to true parameter values).
"""

# conditions under which bootstrap methods suffer?

bs_replicate = np.mean(bs_sample)
print('Boostrap replicate mean (1975) (just one replicate): ', bs_replicate)

bs_replicates_1975 = bs_resample(bd_1975)
bs_replicates_2012 = bs_resample(bd_2012)

plt.figure()
_ = plt.hist(bs_replicates_1975, bins=100, normed=True)
plt.xlabel('mean beak depth (mm)')
plt.ylabel('PDF')
plt.title('1975')
plt.show()

plt.figure()
_ = plt.hist(bs_replicates_2012, bins=100, normed=True)
plt.xlabel('mean beak depth (mm)')
plt.ylabel('PDF')
plt.title('2012')
plt.show()

conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])
print(conf_int_1975)

conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])
print(conf_int_2012)

# how to find the largest confidence interval with which you can separate your distributions?
# would that be bad practice?

# can observe changes in distribution as a function of iteration to test sensitivity

""" Now with the standard deviation """

bs_replicates_1975 = bs_resample(bd_1975, f=np.std)
bs_replicates_2012 = bs_resample(bd_2012, f=np.std)

plt.figure()
_ = plt.hist(bs_replicates_1975, bins=100, normed=True)
plt.xlabel('stddev of beak depth (mm)')
plt.ylabel('PDF')
plt.title('1975')
plt.show()

plt.figure()
_ = plt.hist(bs_replicates_2012, bins=100, normed=True)
plt.xlabel('stddev of beak depth (mm)')
plt.ylabel('PDF')
plt.title('2012')
plt.show()

conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])
print(conf_int_1975)

conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])
print(conf_int_2012)

