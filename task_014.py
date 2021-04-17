#Finding a Shared Motif http://rosalind.info/problems/lcsm/
from Bio import SeqIO


def make_subs(string, key):
    last_position = len(string)
    substrings = []
    for i in range(last_position):
        if key == 'start':
            substrings.append([i, last_position - i])
    return substrings


def find_longes_prefix(template_string, string):
    for i, c in enumerate(template_string):
        if i == len(string):
            return i
        elif i == len(template_string) - 1 and c == string[i]:
            return i + 1
        elif i >= len(string):
            return i
        elif i == len(string) and c == string[i]:
            return i + 1
        elif c == string[i]:
            continue
        elif c != string[i]:
            return i
    

#records = list(SeqIO.parse("rosalind_lcsm.txt", "fasta"))
records = list(SeqIO.parse("dna.txt", "fasta"))
sequences = sorted([record.seq for record in records], key=len)
start = make_subs(sequences[0], key='start')

for string in sequences[1:]:
    subs_pair = len(string)
    for element in start:
        i, j = element[0], element[1]
        last_pos = []
        for pair in range(subs_pair):
            last_pos.append(find_longes_prefix(sequences[0][i:i+j], string[pair:]))
            if last_pos[pair] == len(sequences[0][i:j+i]):
                break    
        element[1] = max(last_pos)

position = max(start, key=lambda x: x[1])
print(sequences[0][position[0]:position[0]+position[1]])
