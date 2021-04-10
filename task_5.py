# Computing GC Content http://rosalind.info/problems/gc/
file = open("rosalind_gc.txt", "r")
line = file.read().strip('>').split('>')
GC = dict()

for i in line:
    name, seq = i.split('\n', 1)
    seq = seq.replace('\n', '')
    GC[name] = ((seq.count('C') + seq.count('G')) / len(seq))*100

name_max, GC_value = max(GC.items(), key = lambda k : k[1])
print(name_max)
print(GC_value)