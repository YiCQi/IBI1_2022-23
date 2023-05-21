# The	script contains	the	variable seq shown above and prints	out	the	correct	number of	coding sequences when	this variable	is modified.

import re

# input custom sequence
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
# three possible stop codons
stop_codon = re.compile(r'TAA|TAG|TGA')
# possible stop positions
stop_pos = re.findall(stop_codon,seq)
# output result
print('number:',len(stop_pos))
