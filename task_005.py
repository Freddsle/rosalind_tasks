# Computing GC Content http://rosalind.info/problems/gc/
with open("rosalind_gc.txt", "r") as f:
    line = f.read().strip('>').split('>')

GC = {}

for i in line:
    name, seq = i.split('\n', 1)
    seq = seq.replace('\n', '')
    GC[name] = ((seq.count('C') + seq.count('G')) / len(seq))

name_max, GC_value = max(GC.items(), key = lambda k : k[1])
print('{}\n{}'.format(name_max,GC_value*100))