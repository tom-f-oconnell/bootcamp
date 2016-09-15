import pytest
import bioinfo_dicts

def n_neg(seq):
    """ Number of negative residues in a protein sequence. """

    seq = seq.upper()
    
    # make sure each character represents a valid amino acid
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid')

    # count E's and D's and return count
    return seq.count('D') + seq.count('E')


