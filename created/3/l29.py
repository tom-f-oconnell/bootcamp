
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

def draw_random_mutation(n_gen, r):
    """ Draws numerically from the random mutation hypothesis underlying distribution.
    (jackpot / Luria-Delbruck distribution) """
    
    # otherwise gain new mutations at a constant proportion
    # always inherit 2 * previous generation mutations
    n_mut = 0

    """
    # of cells that *can* get mutations = 2 * (2^(g-1) - n_mut) = 2^g - 2 * n_mut
    ... and the chance of gaining a mutation is binominally distributed again
    """

    # so r is the mutation rate?
    
    for g in range(n_gen):
        n_mut = 2 * n_mut + np.random.binomial(2**g - 2 * n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    samples = np.empty(size)

    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples


# Specify parameters
# number of generations
n_gen = 16

# chance of having a beneficial mutation
r = 1e-5

# total number of cells
# defining with first gen having one cell
n_cells = 2**(n_gen - 1)

""" The adaptive immunity hypothesis should create a distribution of surviving colonies
    that follow a binomial distribution. """

# adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)

# counts the number of times each integer is encountered
counts = np.bincount(ai_samples)
# plt.clf()
plt.plot(np.arange(len(counts)), counts, marker='.', linestyle='none')
plt.show()

print('AI mean: ', np.mean(ai_samples))
print('AI std: ', np.std(ai_samples))
# according to theory in LD paper, should be about 1
# (because this is true for binomially distributed data)
print('AI Fano: ', np.var(ai_samples) / np.mean(ai_samples))

# TODO seems strange variance in Fano (and std) are still somewhat high
# despite so many iterations
rm_samples = sample_random_mutation(n_gen, r, size=100000).astype(int)

print('RM mean: ', np.mean(rm_samples))
print('RM std: ', np.std(rm_samples))
print('RM Fano: ', np.var(rm_samples) / np.mean(rm_samples))

x_ai, y_ai = ecdf(ai_samples)
x_rm, y_rm = ecdf(rm_samples)

plt.figure()
plt.semilogx(x_ai, y_ai, marker='.', linestyle='none')
plt.semilogx(x_rm, y_rm, marker='.', linestyle='none')
plt.legend(('Adaptive immunity', 'Random mutation'))
plt.show()

