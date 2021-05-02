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
    return i + 1


def pairs_comp(subs_pair, sequences, begin, length, i):
    last_pos = []
    for pair in range(subs_pair):
            last_pos.append(find_longes_prefix(sequences[0][begin:begin+length], sequences[i][pair:]))
            if last_pos[pair] == len(sequences[0][begin:length+begin]):
                break    
    return max(last_pos)


def main():
    records = list(SeqIO.parse("rosalind_gc.txt", "fasta"))
    sequences = sorted([record.seq for record in records], key=len)
    start = make_subs(len(sequences[0]))
    for i in range(1, len(sequences)):
        subs_pair = len(sequences[i])
        for c, (begin, length) in enumerate(start):
            start[c][1] = pairs_comp(subs_pair, sequences, begin, length, i)
    position = max(start, key=lambda x: x[1])
    print(sequences[0][position[0]:position[0]+position[1]])


if __name__ == '__main__':
    main()
