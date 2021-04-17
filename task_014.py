#Finding a Shared Motif http://rosalind.info/problems/lcsm/
from Bio import SeqIO


def make_subs(last_position):
    substrings = []
    for i in range(last_position):
        substrings.append([i, last_position - i])
    return substrings

def find_longes_prefix(template_string, string):
    for i, (letter_tem, letter_str) in enumerate(zip(template_string, string)):
        if letter_tem != letter_str:
            return i
        else:
            continue       
    return i + 1

  
records = list(SeqIO.parse("rosalind_lcsm.txt", "fasta"))
sequences = sorted([record.seq for record in records], key=len)
start = make_subs(len(sequences[0]))

for string in sequences[1:]:
    subs_pair = len(string)
    for c, (begin, length) in enumerate(start):
        last_pos = []
        for pair in range(subs_pair):
            last_pos.append(find_longes_prefix(sequences[0][begin:begin+length], string[pair:]))
            if last_pos[pair] == len(sequences[0][begin:length+begin]):
                break    
        start[c][1] = max(last_pos)

position = max(start, key=lambda x: x[1])
print(sequences[0][position[0]:position[0]+position[1]])
