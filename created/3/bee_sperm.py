
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import stats

weight = pd.read_csv('../../data/bee_weight.csv', comment='#')
sperm = pd.read_csv('../../data/bee_sperm.csv', comment='#')

""" Stats on the weights by treatment. """

# calculate the weight ECDFs
weight_p, wp_cpx = stats.ecdf(weight.loc[weight['Treatment'] == 'Pesticide']['Weight'])
weight_c, wc_cpx = stats.ecdf(weight.loc[weight['Treatment'] == 'Control']['Weight'])

# plot the ECDFs
plt.plot(weight_p, wp_cpx, marker='.', linestyle='none')
plt.plot(weight_c, wc_cpx, marker='.', linestyle='none')
plt.legend(('Pesticide', 'Control'))
plt.title('Does pesticide affect weight?')
plt.xlabel('Weight')
plt.ylabel('ECDF')
plt.margins(0.02)
plt.show()

# b: no clear difference to me

# computing means and 95% bootstrap confidence intervals in the median
print(np.mean(weight_p))
print(np.mean(weight_c))

bs_means_p = stats.bs_resample(weight_p)
bs_means_c = stats.bs_resample(weight_c)

conf_int_pest = np.percentile(bs_means_p, [2.5, 97.5])
conf_int_cont = np.percentile(bs_means_c, [2.5, 97.5])

print('95 percent confidence intervals in means of pesticide treatment group (weight):' + \
      '[{0}, {1}]'.format(*tuple(conf_int_pest)))
print('95 percent confidence intervals in means of control group (weight):' + \
      '[{0}, {1}]'.format(*tuple(conf_int_cont)))

""" Calculations on sperm quality now. """

# calculate the spermq ECDFs
spermq_p, wp_cpx = stats.ecdf(sperm.loc[sperm['Treatment'] == 'Pesticide']\
    ['Quality'].dropna())
spermq_c, wc_cpx = stats.ecdf(sperm.loc[sperm['Treatment'] == 'Control']['Quality'].dropna())

# plot the ECDFs
plt.plot(spermq_p, wp_cpx, marker='.', linestyle='none')
plt.plot(spermq_c, wc_cpx, marker='.', linestyle='none')
plt.legend(('Pesticide', 'Control'))
plt.title('Does pesticide affect sperm quality?')
plt.xlabel('Sperm quality')
plt.ylabel('ECDF')
plt.margins(0.02)
plt.show()

# b: no clear difference to me

# computing means and 95% bootstrap confidence intervals in the median
print(np.mean(spermq_p))
print(np.mean(spermq_c))

bs_means_sq_p = stats.bs_resample(spermq_p)
bs_means_sq_c = stats.bs_resample(spermq_c)

conf_int_sq_mean_pest = np.percentile(bs_means_sq_p, [2.5, 97.5])
conf_int_sq_mean_cont = np.percentile(bs_means_sq_c, [2.5, 97.5])

print('95 percent confidence intervals in means of pesticide treatment group (sperm quality): '+\
      '[{0}, {1}]'.format(*tuple(conf_int_pest)))
print('95 percent confidence intervals in means of control group (sperm quality): ' + \
      '[{0}, {1}]'.format(*tuple(conf_int_cont)))

bs_medians_sq_p = stats.bs_resample(spermq_p, f=np.median)
bs_medians_sq_c = stats.bs_resample(spermq_c, f=np.median)

conf_int_sq_median_pest = np.percentile(bs_medians_sq_p, [2.5, 97.5])
conf_int_sq_median_cont = np.percentile(bs_medians_sq_c, [2.5, 97.5])

print('95 percent confidence intervals in medians of pesticide treatment group (sperm quality): '+\
      '[{0}, {1}]'.format(*tuple(conf_int_sq_median_pest)))
print('95 percent confidence intervals in medians of control group (sperm quality): ' + \
      '[{0}, {1}]'.format(*tuple(conf_int_sq_median_cont)))


