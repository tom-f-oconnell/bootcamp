
""" Caltech programming bootcamp (Summer Bi/Be/NB) Exercise 2 """

import bioinfo_dicts as bd

""" 2.2b Parsing a FASTA file """

def open_fasta():
    """ Returns sequence from salmonella fasta file provided. """

    with open('../data/salmonella_spi1_region.fna','r') as fasta_file:
        data = fasta_file.read().strip().split('>')

    data = [x.split(']\n')[1].replace('\n','') for x in data if len(x) >= 2]

    return data[0]

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

""" 2.4 ORF detection """

def longest_orf(seq):
    """ ORF finding NOT considering open reading frames. 
    Will return None if no ORFs are found. """
    
    stop_codons = {'TGA','TAG','TAA'}
    
    i = 0
    offset = 0
    
    # will be tuples of (offset, start_index)
    maybe_starts = {}

    # should be a tuple of (start_index, stop_codon_first_index)
    longest = None
    longest_length = 0
    
    while i < len(seq) - 3
        
        codon = seq[i:i+3]

        if codon == 'ATG':
            maybe_starts.add((offset, start_index))
    
        elif codon in stop_codons:
           
            # get all start codon indices in same offset
            starts = {start for old_offset, start in maybe_starts \
                if old_offset == offset}

            this_start = min(starts)
            if i - this_start > longest_length:
                longest_length = i - this_start
                longest = (this_start, i)
            
            # remove all putative starts with same offset (there has been a stop)
            maybe_starts = {(off, b) for off, b in maybe_starts if off != offset}

        offset = (offset + 1) % 3

def translation(seq):
    """ Takes a DNA sequence of length multiple of 3, and converts to protein string. """
    
    protein_seq = ''

    for i in range(0,len(seq),3):
        protein_seq += codons[seq[i:i + 3]]

    return protein_seq


""" Run the functions we wrote to get the output missing. """


