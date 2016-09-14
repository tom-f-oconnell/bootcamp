
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

def bs_resample(data, iters=100000, f=np.mean):
   """ Bootstrap resamples the statistic determined by function f (np.mean by default)
   iters times and returns an array of that length. """
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

should_plot = False

bd_1975 = np.loadtxt('../../data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('../../data/beak_depth_scandens_2012.csv')

# Compute ECDFs for 1975 and 2012
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

if should_plot:
    # Plot the ECDFs
    plt.plot(x_1975, y_1975, marker='.', linestyle='none')
    plt.plot(x_2012, y_2012, marker='.', linestyle='none')
    plt.margins(0.02)
    plt.xlabel('beak depth (mm)')
    plt.ylabel('ECDF')
    plt.legend(('1975', '2012'), loc='lower right')
    plt.show()

print('Mean beak size of 1975 population ', np.mean(bd_1975))
print('Mean beak size of 2012 population ', np.mean(bd_2012))

bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))

# Compute ECDF of one bootstrap sample
x_bs, y_bs = ecdf(bs_sample)

if should_plot:
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

if should_plot:
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
print('Confidence interval of 1975 sample mean: ', conf_int_1975)

conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])
print('Confidence interval of 2012 sample mean: ', conf_int_2012)

# how to find the largest confidence interval with which you can separate your distributions?
# would that be bad practice?

# can observe changes in distribution as a function of iteration to test sensitivity

""" Now with the standard deviation """

bs_replicates_1975 = bs_resample(bd_1975, f=np.std)
bs_replicates_2012 = bs_resample(bd_2012, f=np.std)

if should_plot:
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
print('Confidence interval of 1975 sample stddev: ', conf_int_1975)

conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])
print('Confidence interval of 2012 sample stdev: ', conf_int_2012)

""" Equivalence of bootstrap samples and the standard error in the mean """

# bootstrap calculation of the SEM
# (the standard deviation in the estimates of the mean)
bs_sem = np.std(bs_replicates_1975)
print('Bootstrap estimated SEML ', bs_sem)

# the analytic calculation of the SEM
# (the standard deviation divided by the square root of the number of samples)
sem = np.std(bd_1975, ddof=1) / np.sqrt(len(bd_1975))
print('Analytic SEM: ', sem)

""" Further practice (lesson 28) """

x, cpx = ecdf(bd_1975)
_ = plt.plot(x, cpx, color='blue')
plt.xlabel('mean beak depth (mm)')
plt.ylabel('PDF')
plt.title('1975')

n = 10
alphas = np.linspace(1, 0.2, n)
iterations = np.logspace(1, 7, n).astype(int)

print('Planned iterations in order:')
print(iterations)

# calculates the mean, so ECDF of the mean distributions will not
# lie on the original sample ECDF.
for a, i in zip(alphas, iterations):
    print('Bootstrapping with ' + str(i) + ' iterations.')
    bs_replicates_1975 = bs_resample(bd_1975, iters=i)
    bs_x, bs_cpx = ecdf(bs_replicates_1975)
    _ = plt.plot(bs_x, bs_cpx, color='blue', alpha=a)

plt.show()
