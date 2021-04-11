# Computing GC Content http://rosalind.info/problems/gc/
import re

seq, GC = {}, {}
prog = re.compile(r'>Rosalind_\d{4}')

with open("rosalind_gc.txt", "r") as f:
    for line in f:
        line = line.strip('\n') 
        if re.match(prog, line):
            name = line
            seq[name] = [0, 0]               # [len line, GC in line]
        else:
            seq[name][0] += len(line)
            seq[name][1] += line.count('C') + line.count('G')

for element in seq:
    GC[element] = seq[element][1] / seq[element][0]

name_max, GC_value = max(GC.items(), key = lambda k : k[1])
print(f'{name_max}\n{GC_value * 100}')
