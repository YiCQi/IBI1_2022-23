# This code aims to find all sequences ending with input stop codons and create a new file to store the results, including the number of this codon happening in one sequence.

import re

# input custom stop codons
input_seq = input('input(TAA/TGA/TAG):')
# run when input is one of three stop codons
if input_seq == 'TAA' or 'TAG' or 'TGA':
    # input file Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa
    input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
    # output file
    output_file = open(f'{input_seq}_stop_genes.fa', "w")
    # two variables to store the present gene's sequence and name
    now_sequence = ''
    now_gene = ''
    # detect in every line of the file
    for line in input_file:
        # only extract the text
        line = line.strip()
        # detect '>' as the beginning of every gene
        if line.startswith(">"):
            # determine if gene sequence ends with custom stop codon
            if now_sequence.endswith(input_seq):
                # if yes, output
                output_file.write(f">{now_gene}  number:"+str(len(re.findall(input_seq,now_sequence)))+f"\n{now_sequence}\n")
            # get new gene's name
            now_gene = line[1:].split()[0]
            # reset the sequence
            now_sequence = ''
        # if not '>' as beginning, this is a line of sequence
        else:
            now_sequence += line

    # detect the last sequence
    if now_sequence.endswith(input_seq):
        # output
        output_file.write(f">{now_gene}  number:"+str(len(re.findall(input_seq,now_sequence)))+f"\n{now_sequence}\n")

    input_file.close()
    output_file.close()
