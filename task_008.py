#Translating RNA into Protein http://rosalind.info/problems/prot/
from Bio.Seq import Seq

with open("rosalind_prot.txt", "r") as f:
    messenger_rna = Seq(f.read())

protein = messenger_rna.translate()
print(protein)
