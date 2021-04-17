#Finding a Shared Motif http://rosalind.info/problems/lcsm/
from Bio import SeqIO


def make_subs(last_position):
    substrings = []
    for i in range(last_position):
        substrings.append([i, last_position - i])
    return substrings


def find_longes_prefix(template_string, string):
    for i, c in enumerate(template_string):
        if i == len(string):
            return i
        if i == len(template_string) - 1 and c == string[i]:
            return i + 1
        if i >= len(string):
            return i
        if i == len(string) and c == string[i]:
            return i + 1
        if c == string[i]:
            continue
        if c != string[i]:
            return i
    raise NotImplementedError
  

records = list(SeqIO.parse("rosalind_lcsm.txt", "fasta"))
sequences = sorted([record.seq for record in records], key=len)
start = make_subs(len(sequences[0]))

for string in sequences[1:]:
    subs_pair = len(string)
    for c, (begin, lenght) in enumerate(start):
        last_pos = []
        for pair in range(subs_pair):
            last_pos.append(find_longes_prefix(sequences[0][begin:begin+lenght], string[pair:]))
            if last_pos[pair] == len(sequences[0][begin:lenght+begin]):
                break    
        start[c][1] = max(last_pos)

position = max(start, key=lambda x: x[1])
print(sequences[0][position[0]:position[0]+position[1]])
