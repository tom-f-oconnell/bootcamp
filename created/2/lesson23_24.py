
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ecdf(x):
    print(x)

data = np.loadtxt('../../data/collins_switch.csv', delimiter=',', skiprows=2)

iptg = data[:,0]
gfp = data[:,1]
sem = data[:,2]

# contrary to what the bootcamp website says, the second column is the one that (seems) to have
# been normalized

#plt.plot(iptg, gfp, marker='.', linestyle='none')
plt.semilogx(iptg, gfp, marker='.', linestyle='none')
plt.xlabel('IPTG concentration')
plt.ylabel('Normalized GFP fluorescence intensity')
plt.show()

# now with error bars
plt.errorbar(iptg, gfp, yerr=sem, marker='.', markersize='10', linestyle='none')
plt.xlabel('IPTG concentration')
plt.ylabel('Normalized GFP fluorescence intensity')
plt.xscale('log')
plt.show()

