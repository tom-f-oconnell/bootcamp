
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.optimize as sopt

def gradient_model(x, I_0, a, lam):
    """ Model for Bcd gradient: exponential decay plus a constant background. """

    assert np.any(np.array(x) >= 0)
    assert np.any(np.array([I_0, a, lam]) >= 0)

    return a + I_0 * np.exp(-x / lam)

df = pd.read_csv('../../data/bcd_gradient.csv', comment='#')
df = df.rename(columns={'fractional distance from anterior': 'x', '[bcd] (a.u.)': 'I_bcd'})

plt.plot(df['x'], df['I_bcd'], marker='.', linestyle='none')
plt.show()

a_guess = 0.2
I_0_guess = 0.9 - 0.2
lam_guess = 0.25
p0 = np.array([I_0_guess, a_guess, lam_guess])

popt, _ = sopt.curve_fit(gradient_model, df['x'], df['I_bcd'], p0=p0)

x_smooth = np.linspace(0, 1, 200)

I_smooth = gradient_model(x_smooth, *tuple(popt))

plt.plot(x_smooth, I_smooth, color='gray')
