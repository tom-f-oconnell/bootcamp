
import numpy as np

high = np.loadtxt('../../data/xa_high_food.csv')
low = np.loadtxt('../../data/xa_low_food.csv')

def xa_to_diam(xa):
    """ Converts circular cross sectional area to the circle's diameter """

    return 2 * np.sqrt(xa / np.pi)
