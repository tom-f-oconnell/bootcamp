
""" Caltech programming bootcamp (Summer Bi/Be/NB) Exercise 2 """

""" 2.2b Parsing a FASTA file """

with open('../data/aligned.fasta','r') as fasta_file:
    data = fasta_file.read().strip().split('>')

data = [x.split(']\n')[1].replace('\n','') for x in data if len(x) >= 2]

# a list of as many sequences as were in the FASTA file
print(data)

""" 2.3 Pathogenicity islands """

def gc_blocks(seq, block_size):
    """ Computes GC content in non-overlapping blocks. Blocks less than size are ignored. """
    
    contents = []
    i = block_size
    while i < len(seq):
        count = 0

        for base in seq[i - block_size:i]:
            if base == 'C' or base == 'G':
                count += 1

        contents.append(count / block_size)

    return tuple(contents)


def gc_map(seq, block_size, gc_thresh):
    """ Capitalizes all bases in blocks above gc_thresh GC content, and lowercases others. """

    contents = gc_blocks(seq, block_size)

    # break the sequence into regions of block length
    # should be same length as `contents`
    mapped = [seq[x:block_size] for x in range(0,len(seq),block_size) \
        if len(seq[x:block_size]) == block_size]

    for i, content in contents:
         
        # capitalize every block over threshold
        if content > gc_thresh:
            mapped[i] = mapped[i].upper()
        else:
            mapped[i] = mapped[i].lower()
    
    return ''.join(mapped)


