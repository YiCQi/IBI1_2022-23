# write	a function that	determines whether a given DNA sequence	is likely to be	protein-coding or not.
import re
def calculator(dna):
    # store the length of DNA
    length = len(dna)
    # find opening and final codon in DNA (assume there is only one opening/final codon)
    opening = [codon.start() for codon in re.finditer(r'[Aa][Tt][Gg]',dna)][0]
    final = [codon.start() for codon in re.finditer(r'[Tt][Gg][Aa]',dna)][0]
    # calculate the distance between opening and final codons
    distance = final-opening
    print(distance)
    # calculate the percentage of coding sequence in DNA
    percentage = distance/length
    # determine the type
    if percentage >= 0.5:
        label = 'protein_coding'
    elif percentage <= 0.1:
        label = 'non-coding'
    else:
        label = 'unclear'
    return percentage,label

# example
print(calculator('TtAtaGaTGcCTaTCaTatGA'))
