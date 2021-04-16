#Overlap Graphs http://rosalind.info/problems/grph/
from Bio import SeqIO

fasta = {}
seq = ''
answer = []

for line in SeqIO.parse("rosalind_grph.txt", "fasta"):
    seq = line.seq[:3] + line.seq[-3:]
    fasta[line.id] = seq

for first in fasta:
    for second in fasta:
        if first != second and fasta[first][-3:] == fasta[second][:3]:
            answer.append([first, second])

with open("myfile.txt", "w") as f:
    for elenemt in answer:
        print(elenemt[0], elenemt[1], file=f)
