
""" Solutions to exercise 1 questions from Bi/Be/NB 203 """

import random
import numpy as np

""" For 1.3 """

def random_seq(length, nucleic_acid='DNA'):
    """ Generates a random sequence of DNA or RNA of a given length """
    
    if nucleic_acid == 'DNA':
        alphabet = ('A','C','T','G')
    elif nucleic_acid == 'RNA':
        alphabet = ('A','C','U','G')

    so_far = ''
    for i in range(length):
        so_far += random.sample(alphabet, 1)[0]
    return so_far

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

def revcomp_a(s, nucleic_acid='DNA'):
    """ Solution to 1.3a. """
    ret = ''
    for c in s[::-1]:
        ret += complement_base(c, material=nucleic_acid)
    return ret

def revcomp_b(s, nucleic_acid='DNA'):
    """ Solution to 1.3b. """

    if nucleic_acid == 'DNA':
        # switch A's and T's
        s = s[::-1].replace('A','B')
        s = s.replace('T','A')
        s = s.replace('B','T')
    elif nucleic_acid == 'RNA':
        # switch A's and U's
        s = s[::-1].replace('A','B')
        s = s.replace('U','A')
        s = s.replace('B','U')

    # switch C's and G's
    s = s.replace('C','B')
    s = s.replace('G','C')
    return s.replace('B','G')

""" For 1.4 """

def score(c1, c2):
    """ Defines a score for a pair of characters
    for dynamic programming scoring of total subsequence. """
    if c1 == c2:
        return 1
    else:
        return 0

def lcs(s1, s2):
    """ Finds the longest common subSTRING between two strings via dynamic programming.
    Returns dynamic programming table and array for tracking local moves.
    NOTE: substring =/= subsequence. substrings are contiguous. """

    shape = (len(s1) + 1, len(s2) + 1)
    M = np.zeros(shape)

    max_length_so_far = 0
    candidates = set()

    for i in range(len(s1)):
        for j in range(len(s2)):

            if s1[i] == s2[j]:
                M[i+1,j+1] = M[i,j] + 1

                if M[i+1,j+1] > max_length_so_far:
                    max_length_so_far = int(M[i+1,j+1])
                    candidates = {s1[i - max_length_so_far + 1: i + 1]}

                elif M[i+1,j+1] == max_length_so_far:
                    candidates.add(s1[i - max_length_so_far + 1: i + 1])

            else:
                M[i,j] = 0

    candidates.add('')

    return candidates

""" For exercise 1.5 """

def valid_secondary_RNA(seq):
    return False

""" Run exercise 1.3 code """

test_iterations = 100
# could also do random.sample(range(10), k) + [0]
lengths = range(10)

for nuc in ('DNA', 'RNA'):
    for length in lengths:
        for i in range(test_iterations):
            seq = random_seq(length, nucleic_acid=nuc)
            # don't need to worry about mutability because seq is a string
            s1 = revcomp_a(seq, nucleic_acid=nuc)
            s2 = revcomp_b(seq, nucleic_acid=nuc)
            """
            print(seq)
            print(s1)
            print(s2)
            """
            assert s1 == s2
            print('Reverse complement of ' + seq + ' is ' + s1)

print('No inconsistencies between my two reverse complement algorithms.')

""" Run exercise 1.4 code """

max_length = 1000
samples = 10
s1_lengths = random.sample(range(max_length),samples) + [0]
s2_lengths = random.sample(range(max_length),samples) + [0]

for i in range(test_iterations):
    for len1, len2 in zip(s1_lengths, s2_lengths):
        s1 = random_seq(len1)
        s2 = random_seq(len2)

        # + 1 since otherwise length of minimum length string would be excluded as a 
        # possible lcs length
        min_len = min(len1,len2)
        lcs_length = random.choice(range(min_len + 1))
        lcs_offset1 = random.choice(range(len(s1) - lcs_length + 1))
        lcs_offset2 = random.choice(range(len(s2) - lcs_length + 1))

        # doesn't matter which string we copy from since each is generated randomly
        # artificially give the strings what is ***likely*** going to be an LCS (not always)
        # ...not likely for 0 case though, or perhaps other low string lengths

        s1 = s1[:lcs_offset1] + s2[lcs_offset2:lcs_offset2 + lcs_length] + \
            s1[lcs_offset1 + lcs_length + 1:]
        
        candidates = lcs(s1,s2)
        print('S1, S2, and their LCS(s) determined w/ dynamic programming')
        print(s1)
        print(s2)
        print(candidates)


""" Run exercise 1.5 code """
