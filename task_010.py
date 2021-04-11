#Consensus and Profile http://rosalind.info/problems/cons/
import re

answer = ''
kb = 1000
alphabet = ['A', 'C', 'G', 'T']
Profile = {'A': [0] * kb,
           'C': [0] * kb,
           'G': [0] * kb,
           'T': [0] * kb}

with open("rosalind_cons.txt", "r") as f:
    for line in f:
        if re.match(r'>Rosalind_\d{4}', line):
            j = 0
        else:
            for i, c in enumerate(line.strip('\n')):
                Profile[c][i+j] += 1
            j += len(line) - 1
            
for i in range(kb):
    l = (Profile['A'][i], 
         Profile['C'][i],
         Profile['G'][i], 
         Profile['T'][i])
    if sum(l) != 0:
        index = l.index(max(l))
        answer += alphabet[index]

with open("myfile.txt", "w") as f:
    print(answer,
        '\nA: ', *Profile['A'][:j],
        '\nC: ', *Profile['C'][:j], 
        '\nG: ', *Profile['G'][:j], 
        '\nT: ', *Profile['T'][:j], 
        file=f)
