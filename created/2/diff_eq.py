
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

""" Simple Euler updating ODE model of exponential bacterial growth """

# Specify parameter
k = 1

# Specify my little time step
delta_t = 0.01

# Make an array of time points, evenly spaced up to 10
t = np.arange(0, 10, delta_t)

# Make an array to store the number of bacteria
n = np.empty_like(t)

# Set the initial number of bacteria
n[0] = 1

# Write a for loop to keep updating n as time goes on
for i in range(1, len(t)):
    n[i] = n[i-1] + delta_t * k * n[i-1]

plt.plot(t, n)
plt.margins(0.02)
plt.xlabel('Time')
plt.ylabel('Number of bacteria')
plt.show()

""" Same for a Lotke-Volterra population model with foxes (f) and rabbits (r) """

plt.figure()

alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001
t = np.arange(0, 60, delta_t)
r = np.empty_like(t)
f = np.empty_like(t)
r[0] = 10
f[0] = 1

for i in range(1, len(t)):
    r[i] = r[i-1] + delta_t * alpha * r[i-1] - delta_t * beta * f[i-1] * r[i-1]
    f[i] = f[i-1] + delta_t * delta * f[i-1] * r[i-1] - delta_t * gamma * f[i-1]

f, = plt.plot(t, f, color='red', label='Foxes')
r, = plt.plot(t, r, color='black', label='Rabbits')
plt.margins(0.02)
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(handles=[f, r])
plt.show()
