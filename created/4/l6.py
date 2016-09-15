import pytest

def find_codon_lesson6(codon, seq):
    """Find a specified codon with a given sequence.""" 

    if not len(codon) == 3:
        raise RuntimeError('codon needs to be 3 bases long')

    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        print(seq[i:i+3])
        
        i += 3
    
        if i >= len(seq):
            return -1
                
    return i
