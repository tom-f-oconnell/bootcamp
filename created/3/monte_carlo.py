
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import stats

# website says tau (step time) is about 0.5 sec, but we just care about steps for now
def backtrack_steps():
    t = 0
    x = 0

    directions = np.array([-1, 1], dtype=int)

    while x <= 0:
        x = x + np.random.choice(directions)
        t += 1

    return t

def gen_backtracks(n=10000):
    bt_reps = np.empty(n)

    for i in range(n):
        #print(i)
        bt_reps[i] = backtrack_steps()

    return bt_reps

# binsize again?
bts = gen_backtracks()

plt.hist(gen_backtracks(), normed=True)
plt.title('Backtrack step counts on pause')
plt.show()

bt_sorted, bt_cpf = stats.ecdf(bts)



