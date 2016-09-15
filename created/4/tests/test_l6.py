import pytest
import l6

def test_find_codon_lesson6():
    seq = '''ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAACAATGCAGCCCAGAAGA
    AGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCT
    GGAGCGGGACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTC
    GAGCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATTCTGGGCG
    TGATAGCCGTTGTGCTGCTCATCATCGTTCTGGTGTCGCTTTTCAATTGA'''.replace('\n','')

    codon = 'ATG'
    # 0 because we only find the first such codon
    # should be able to find a codon in the first position
    assert l6.find_codon_lesson6(codon, seq) == 0

    # codons must be 3 bases long
    pytest.raises(RuntimeError, "l6.find_codon_lesson6('', '') == 0")
    pytest.raises(RuntimeError, "l6.find_codon_lesson6('A', '') == 0")
    pytest.raises(RuntimeError, "l6.find_codon_lesson6('AT', '') == 0")
    pytest.raises(RuntimeError, "l6.find_codon_lesson6('ATGG', '') == 0")

    pytest.raises(RuntimeError, "l6.find_codon_lesson6('', seq) == 0")
    pytest.raises(RuntimeError, "l6.find_codon_lesson6('A', seq) == 0")
    pytest.raises(RuntimeError, "l6.find_codon_lesson6('AT', seq) == 0")
    pytest.raises(RuntimeError, "l6.find_codon_lesson6('ATGG', seq) == 0")

    # must be in register with start codon
    # in register
    assert l6.find_codon_lesson6('AGG', 'ATGAGCCTCAGGC') == 9
    # not in register. -1 for not found.
    assert l6.find_codon_lesson6('AGG', 'ATGAGCCCTCAGGC') == -1
    
    # should be able to find a codon in the last position
    assert l6.find_codon_lesson6('AGG', 'ATGAGG') == 3
