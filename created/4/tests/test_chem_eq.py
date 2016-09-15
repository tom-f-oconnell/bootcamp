
import pytest
import numpy as np
import chem_eq

def test_eq_concs():
    Kd = 10
    ca_0 = 5
    cb_0 = 11
    ca, cb, cab = chem_eq.eq_concs(Kd, ca_0, cb_0)

    assert np.close(Kd, (ca * cb) / cab)

    assert ca >= 0 and cb >= 0 and cab >= 0
