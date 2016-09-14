
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """ Computes fold change in concentration. c can be a scalar or numpy array. 
    The RK ratio must be a scalar. """
    num = RK * (1 + c / KdA)**2
    den = (1 + c / KdA)**2 + Kswitch * (1 + c / KdI)**2
    return 1 / (1 + (num / den))

def fold_change_bohr(bohr_parameter):
    """ Gives the fold change as a function of the bohr parameter. """

    return 1 / (1 + np.exp((-1) * bohr_parameter))

def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """ Calculates the Bohr parameter (concentration dependent) from some known
    properties about the allosteric molecule. """

    # the natural log
    term1 = (-1) * np.log(RK)
    num = (1 + c / KdA)**2
    denom = (1 + c / KdA)**2 + Kswitch * (1 + c / KdI)**2
    term2 = np.log(num / denom)
    return term1 - term2
    

# load the data
wt = np.loadtxt('../../data/wt_lac.csv', delimiter=',', skiprows=3)
q18m = np.loadtxt('../../data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a = np.loadtxt('../../data/q18a_lac.csv', delimiter=',', skiprows=3)

# separate out the [IPTG] (mM) and experimental fold change
wt_iptg = wt[:,0]
wt_fc = wt[:,1]

q18m_iptg = q18m[:,0]
q18m_fc = q18m[:,1]

q18a_iptg = q18a[:,0]
q18a_fc = q18a[:,1]

# plot experimental data
e1, = plt.semilogx(wt_iptg, wt_fc, marker='.', linestyle='none', color='r', label='WT empirical')
e2, = plt.semilogx(q18m_iptg, q18m_fc, marker='.', linestyle='none', color='g', \
    label='q18m empirical')
e3, = plt.semilogx(q18a_iptg, q18a_fc, marker='.', linestyle='none', color='b', \
    label='q18a empirical')

# better title?
plt.title('Fold change in expression by IPTG concentration, for 3 genotypes')
plt.xlabel('[IPTG] (mM)')
plt.ylabel('Fold change in lac expression')
plt.margins(0.02)

# fit fold change with parameters determined externally
faux_iptg = np.logspace(-5,1,num=len(wt_iptg)*2)

wt_RK_ratio = 141.5 # mM^-1
wt_fit = np.array([fold_change(c, wt_RK_ratio) for c in faux_iptg])

q18m_RK_ratio = 1328  # mM^-1
q18m_fit = np.array([fold_change(c, q18m_RK_ratio) for c in faux_iptg])

q18a_RK_ratio = 16.56 # mM^-1
q18a_fit = np.array([fold_change(c, q18a_RK_ratio) for c in faux_iptg])

# TODO how to add note, so as to not repeat Theoretical / Empirical? 
t1, = plt.semilogx(faux_iptg, wt_fit, color='r', alpha=0.5, label='WT theoretical')
t2, = plt.semilogx(faux_iptg, q18m_fit, color='g', alpha=0.5, \
    label='q18m theoretical')
t3, = plt.semilogx(faux_iptg, q18a_fit, color='b', alpha=0.5, \
    label='q18a theoretical')

plt.legend(handles=[e1,t1,e2,t2,e3,t3], loc='lower right')
plt.show()

""" Plot `Data collapse` illustration with Bohr parameter and fold change equation. """

plt.figure()
x = np.linspace(-6, 6, 1000)

# on the same plot?
t, = plt.plot(x, np.array([fold_change_bohr(i) for i in x]), color='gray', label='Theoretical')
plt.title('Fold changes resulting from a range of Bohr parameters')
plt.xlabel('Bohr parameter')
plt.ylabel('Fold change')
plt.margins(0.02)

""" Now fit this model with the experimental data. """
r, = plt.plot(np.array([bohr_parameter(c, wt_RK_ratio) for c in wt_iptg]), wt_fc, marker='.', \
    color='r', linestyle='none', label='WT')
g, = plt.plot(np.array([bohr_parameter(c, q18m_RK_ratio) for c in q18m_iptg]), q18m_fc, \
    marker='.', color='g', linestyle='none', label='q18m')
b, = plt.plot(np.array([bohr_parameter(c, q18a_RK_ratio) for c in q18a_iptg]), q18a_fc, \
    marker='.', color='b', linestyle='none', label='q18a')

plt.legend(handles=[t,r,g,b], loc='lower right')
plt.show()

