
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

rerun_simulation = False
filename = '../../data/my_pause_steps.csv'

if rerun_simulation:
    # binsize again?
    bts = gen_backtracks()

    # doesn't illustrate the power law distributed data very well
    #plt.hist(gen_backtracks(), normed=True)
    #plt.title('Backtrack step counts on pause')
    #plt.show()

    bt_sorted, bt_cpf = stats.ecdf(bts)
    
    # turn the recorded step counts into a DataFrame
    d = {'steps until +1': bts}
    df = pd.DataFrame(data=d)

    # save the data as a DataFrame to save it in a manner consistent with theme today
    df.to_csv(filename, index=False)

if not rerun_simulation:
    df = pd.read_csv(filename)

# determine a reasonable range to plot the histogram over
max_pwr = np.log(df['steps until +1'].max()) / np.log(10)

plt.hist(df['steps until +1'], bins=np.logspace(0, max_pwr, 50))
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.show()
