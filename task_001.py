#Counting DNA Nucleotides http://rosalind.info/problems/dna/
import collections

with open("dna.txt", "r") as f:
    dna_text = f.read()

counter = collections.Counter(dna_text)
print(counter['A'], ' ', counter['C'], ' ', counter['G'], ' ', counter['T'])