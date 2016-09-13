
def complement_base(base,material='DNA'):
    """ Return the Watson-Crick complement of a base."""
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def compliment_base(base):
    """ Do something else. """
    return 'hey base, you lookin good'

def rev_comp(seq):
    ret = ''
    for base in reversed(seq):
        ret += complement_base(base)
    return ret

print(rev_comp('ACTGTGTGTGTGGGGGGGTTTTTTAAAAA'))
