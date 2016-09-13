

codon = 'AUG'
stop_codons = {'UGA', 'UAA', 'UAG'}

if codon == 'AUG':
    print('This codon is the start codon')
elif codon in stop_codons:
    print('This codons is a stop codon')
else:
    print('Neither.')


