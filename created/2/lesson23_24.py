
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import bootcamp_utils as bu

show_1and2 = False
show_food_ecdfs = True

data = np.loadtxt('../../data/collins_switch.csv', delimiter=',', skiprows=2)

iptg = data[:,0]
gfp = data[:,1]
sem = data[:,2]

# contrary to what the bootcamp website says, the second column is the one that (seems) to have
# been normalized

if show_1and2:
    #plt.plot(iptg, gfp, marker='.', linestyle='none')
    plt.semilogx(iptg, gfp, marker='.', linestyle='none')
    plt.xlabel('IPTG concentration')
    plt.ylabel('Normalized GFP fluorescence intensity')
    plt.show()

# now with error bars
if show_1and2:
    plt.errorbar(iptg, gfp, yerr=sem, marker='.', markersize='10', linestyle='none')
    plt.xlabel('IPTG concentration')
    plt.ylabel('Normalized GFP fluorescence intensity')
    plt.xscale('log')
    plt.show()

# now the ecdfs of the food data we were working with earlier
# load food data
high = np.loadtxt('../../data/xa_high_food.csv')
low = np.loadtxt('../../data/xa_low_food.csv')

xhigh, yhigh = bu.ecdf(high)
xlo, ylo = bu.ecdf(low)

if show_food_ecdfs:
    plt.plot(xhigh, yhigh, marker='.', linestyle='none')
    plt.title('High food')
    plt.xlabel('Egg cross sectional area (um$^2$)')
    plt.ylabel('Cumulative probability')
    plt.show()

if show_food_ecdfs:
    plt.figure()
    plt.plot(xlo, ylo, marker='.', linestyle='none')
    plt.title('Low food')
    plt.xlabel('Egg cross sectional area (um$^2$)')
    plt.ylabel('Cumulative probability')
    plt.show()


