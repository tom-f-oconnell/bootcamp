
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.optimize as sopt

def gradient_model(x, I_0, a, lam):
    """ Model for Bcd gradient: exponential decay plus a constant background. """

    assert np.all(np.array(x) > 0)
    assert np.all(np.array([I_0, a, lam]) >= 0)

    return a + I_0 * np.exp(-x / lam)

df = pd.read_csv('../../data/bcd_gradient.csv', comment='#')
df = df.rename(columns={'fractional distance from anterior': 'x', '[bcd] (a.u.)': 'I_bcd'})

plt.plot(df['x'], df['I_bcd'], marker='.', linestyle='none')
plt.show()

