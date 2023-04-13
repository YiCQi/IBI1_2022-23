import re

# input custom sequence
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
# three possible stop codons
stop_codon = re.compile(r'TAA|TAG|TGA')
# possible stop positions
stop_pos = re.findall(stop_codon,seq)
# output result
print('number:',len(stop_pos))
