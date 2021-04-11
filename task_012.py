#Overlap Graphs http://rosalind.info/problems/grph/
import re

prog = re.compile(r'>Rosalind_\d{4}')
seq = {}
name, fasta = '', ''
name_prev, line_prev = '', ''
answer = []

with open("rosalind_grph.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        if re.match(prog, line):
            if name != '':
                name_prev = name
            name = line[1:]
            i = 0
        elif i == 0:
            seq[name] = line[:3]
            if line_prev != '':
                seq[name_prev] += line_prev[-3:]
            i += 1
            line_prev = line
        else:
            line_prev = line
    seq[name] += line_prev[-3:]

for first in seq:
    for second in seq:
        if first != second and seq[first][-3:] == seq[second][:3]:
            answer.append([first, second])

with open("myfile.txt", "w") as f:
    for elenemt in answer:
        print(elenemt[0], elenemt[1], file=f)
