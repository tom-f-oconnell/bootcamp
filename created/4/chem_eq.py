
""" Practice 2: a chemical equilibrium calculator """

"""
Given: Kd, ca_0, and cb_0
Want to calculate: ca, cb, and cab at equilibrium
"""
def eq_concs(Kd, ca_0, cb_0):
    cab = (1/2) * (ca_0 + cb_0 + Kd - np.sqrt((ca_0 + cb_0 + Kd)**2 - 4 * ca_0 * cb_0))
    ca = ca_0 - cab
    cb = cb_0 - cab
