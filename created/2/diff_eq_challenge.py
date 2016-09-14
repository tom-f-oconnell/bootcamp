
# NumPy and odeint, our workhorses
import numpy as np
import scipy.integrate

# Plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

def lotka_volterra_rhs(fr, t, alpha, beta, gamma, delta):
    """
    Right hand side for the Lotka-Volterra population model with foxes (f) and rabbits (r).
    """
    f, r = fr
    df_dt = delta * f * r - gamma * f
    dr_dt = alpha * r - beta * f * r

    # print('stepping equations with df/dt=', df_dt, ' and dr/dt=', dr_dt)

    return np.array([df_dt, dr_dt])

# Magic function to make matplotlib inline; other style specs must come AFTER
# %matplotlib inline

# This enables high res graphics inline
# %config InlineBackend.figure_formats = {'png', 'retina'}

# JB's favorite Seaborn settings for notebooks
rc = {'lines.linewidth': 2, 
      'axes.labelsize': 18, 
      'axes.titlesize': 18, 
      'axes.facecolor': 'DFDFE5'}

sns.set_context('notebook', rc=rc)
sns.set_style('darkgrid', rc=rc)

alpha = 1
beta = 0.2
gamma = 0.8
delta = 0.3
args = (alpha, beta, gamma, delta)

delta_t = 0.001
t = np.arange(0, 60, delta_t)

# initial conditions
fr_0 = np.array([10.0, 1.0])

fr = scipy.integrate.odeint(lotka_volterra_rhs, fr_0, t, args=args)

f = fr[:,0]
r = fr[:,1]

f, = plt.plot(t, f, color='red', label='Foxes')
r, = plt.plot(t, r, color='black', label='Rabbits')
plt.margins(0.02)
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(handles=[f, r])
plt.show()
