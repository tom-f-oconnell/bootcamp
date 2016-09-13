import bioinfo_dicts

def one_to_three(seq):
    seq = seq.upper()

    # build conversion
    aa_list = []
    for aa in seq:
        if aa in bioinfo_dics.aa.keys():
            aa_list += [bioinfo_dicts.aa[aa]]
        else:
            raise RuntimeError(aa + ' is not a valid amino acid.')

    return '-'.join(aa_list)


try:
    import gc_content
    have_gc = True
except ImportError as e:
    have_gc = False

seq = 'ACGTAGCTGATGATAAATCGCCCATATGACTG'

if have_gc:
    print(gc_content.gc(seq))
else:
    print(seq.count('G') + seq.count('C') / len(seq))
