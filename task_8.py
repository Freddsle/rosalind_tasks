#Translating RNA into Protein http://rosalind.info/problems/prot/
from Bio.Seq import Seq

file = open("rosalind_prot.txt", "r")
messenger_rna = Seq(file.read())
protein = messenger_rna.translate()
print(protein)
