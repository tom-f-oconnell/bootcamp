
import numpy as np

def ecdf(x):
    """ Computes empirical cumulative probability distribution for data x. """
    
    x_sorted = np.sort(x)
    # give each element equal incremental probability
    y = np.linspace(0,1,len(x))
    return (x_sorted, y)
