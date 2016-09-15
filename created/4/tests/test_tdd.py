import pytest

import tdd

def test_n_neg():
    assert tdd.n_neg('E') == 1
    assert tdd.n_neg('D') == 1
    assert tdd.n_neg('') == 0
    assert tdd.n_neg('ACKLWTTAE') == 1
    assert tdd.n_neg('DEDEDDEE') == 8
    assert tdd.n_neg('acklwttae') == 1
    assert tdd.n_neg('A') == 0
    assert tdd.n_neg('a') == 0

    # only allow 20 naturally occuring amino acids
    # Z is one example of an invalid amino acid
    pytest.raises(RuntimeError, "tdd.n_neg('Z')")

    print('Test passed.')
