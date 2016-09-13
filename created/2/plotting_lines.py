
import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(-15, 15, 400)

# compute normalized intensity
# using j1=1st order Bessel function from scipy
norm_I = 4 * (scipy.special.j1(x) / x)**2

plt.plot(x, norm_I, marker='.', linestyle='none')
# expands margins be 2%
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x) / I_0$')
plt.show()

# close all plots
plt.close()

# now the Meister spike data
data = np.loadtxt('../../data/retina_spikes.csv', skiprows=2, delimiter=',')
t = data[:,0]
v = data[:,1]

plt.plot(t, v)
plt.xlabel('t (ms)')
plt.ylabel('V (uV)')
plt.xlim(1395, 1400)
plt.show()


