
""" Caltech programming bootcamp (Summer Bi/Be/NB) Exercise 2 """

import bioinfo_dicts as bd
import os

""" 2.2b Parsing a FASTA file """

def open_fasta(seq_file, want_prefix=False):
    """ Returns sequence from fasta file provided. """

    with open(seq_file, 'r') as fasta_file:
        # the first line should be the metadata if there is just one seq
        prefix = fasta_file.readline()
        data = fasta_file.read().strip().replace('\n','')

    if want_prefix:
        return (prefix, data)
    else:
        return data

""" 2.3 Pathogenicity islands """

def gc_blocks(seq, block_size):
    """ Computes GC content in non-overlapping blocks. Blocks less than size are ignored. """
    
    contents = []
    i = block_size
    while i < len(seq) - block_size:
        count = 0

        for base in seq[i - block_size:i]:
            if base == 'C' or base == 'G':
                count += 1

        contents.append(count / block_size)

        i += block_size

    return tuple(contents)


def gc_map(seq, block_size, gc_thresh):
    """ Capitalizes all bases in blocks above gc_thresh GC content, and lowercases others. """

    contents = gc_blocks(seq, block_size)

    # break the sequence into regions of block length
    # should be same length as `contents`
    mapped = []

    for i in range(0, len(seq) // block_size):
        start = i * block_size
        mapped += [seq[start: start + block_size]]
    
    for i, content in enumerate(contents):
         
        # capitalize every block over threshold
        if content > gc_thresh:
            mapped[i] = mapped[i].upper()
        else:
            mapped[i] = mapped[i].lower()
    
    return ''.join(mapped)

""" 2.4 ORF detection """

def longest_orf(seq, n=1):
    """ ORF finding NOT considering open reading frames. 
    Will return None if no ORFs are found. """
    
    stop_codons = {'TGA','TAG','TAA'}
    
    i = 0
    offset = 0
    cutoff_length = 0
    
    # will be tuples of (offset, start_index)
    maybe_starts = set()

    # should be a tuple of (start_index, stop_codon_first_index)
    longest = dict()
    
    while i < len(seq) - 3:
        codon = seq[i:i+3]
        
        if codon == 'ATG':
            maybe_starts.add((offset, i))
         
        elif codon in stop_codons:
           
            # get all start codon indices in same offset
            starts = {start for old_offset, start in maybe_starts \
                if old_offset == offset}
            
            # see if any current ORFs can contend with current n largest
            if len(starts) > 0:
                # the earliest start in frame will yield the single longest
                # but there could also be several of the n longest in frame here
                # TODO ignoring above case for now, for simplicity
                this_start = min(starts)

                if len(longest) < n:
                    longest[i - this_start] = (this_start, i)

                elif i - this_start > cutoff_length:
                    longest.pop(cutoff_length)
                    longest[i - this_start] = (this_start, i)

                cutoff_length = min(longest.keys())
                
                # remove all putative starts with same offset (there has been a stop)
                maybe_starts = {(off, b) for off, b in maybe_starts if off != offset}

        offset = (offset + 1) % 3
        i += 1

    if len(longest) == 0:
        return None
    else:
        orfs = []
        for key in longest:
            start, end = longest[key]
            orfs.append(seq[start:end])
        return orfs

def translation(seq):
    """ Takes a DNA sequence of length multiple of 3, and converts to protein string. """
    
    protein_seq = ''

    for i in range(0,len(seq),3):
        protein_seq += bd.codons[seq[i:i + 3]]

    return protein_seq


""" Run the functions we wrote to get the output missing. """

# 2.3c

_output = False

thresh = 0.45
block_size = 1000
prefix, seq = open_fasta('../data/salmonella_spi1_region.fna', want_prefix=True)

mapped_seq = gc_map(seq, block_size, thresh)

if _output:
    output = '../data/gcmapped_salmonella.fna'
    if os.path.isfile(output):
        raise FileExistsError(output + ' already exists')

    width =  60

    # add the newlines back to the sequence (every 60 characters)
    all_but_tail = ''.join([mapped_seq[i:i + width] + '\n' for i in range(0, len(seq), width)])

    with open(output, 'w') as f:
        f.write(prefix + all_but_tail)

# 2.4

longest = longest_orf(seq)[0]
protein = translation(longest)
print('Single longest ORF, translated:')
print(protein)

# searching w/ blastp for the above sequence, it seems it is a...
# "two-component sensor histidine kinase BarA [Salmonella enterica]"

print('Five longest ORFs, translated:')
longest = longest_orf(seq, n=5)
translations = [translation(x) for x in longest]
print(translations)
