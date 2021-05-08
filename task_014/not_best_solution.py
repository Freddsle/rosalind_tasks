#Finding a Shared Motif http://rosalind.info/problems/lcsm/
#Run with "python -m task_014.not_best_solution"
import itertools
from Bio import SeqIO
from my_utils import my_timer


def make_subs(sequence):
    last_position = len(sequence)
    substrings = []
    for i in range(last_position):
        substrings.append([i, last_position - i])
    return substrings

 
def find_longes_prefix(needle, needle_positions, haystack, begin_haystack, len_haystack):
    for i, k in zip(range(needle_positions[0], needle_positions[0]+needle_positions[1]), 
                    range(needle_positions[0] + needle_positions[1])):
        if len_haystack > begin_haystack+k:
            if needle[i] != haystack[begin_haystack+k]:
                return k
        elif len_haystack == begin_haystack+k:
            return k
    return k + 1


def strings_comparison(needle, needle_positions, haystack):
    last_pos = []
    len_haystack = len(haystack)
    for begin_haystack in range(len_haystack):
        last_pos.append(find_longes_prefix(needle, needle_positions, haystack, 
                        begin_haystack, len_haystack))
    return max(last_pos)


@my_timer
def main():
    records = list(SeqIO.parse("rosalind_lcsm.txt", "fasta"))
    sequences = sorted([record.seq for record in records], key=len)
    
    for i, string in enumerate(sequences):
        if i == 0:
            substrings = make_subs(sequences[0])
            needle = sequences[0]
        else:
            for c, needle_positions in enumerate(substrings):
                if substrings[c][1] > 0:
                    print(strings_comparison(needle, needle_positions, string))
                    substrings[c][1] = strings_comparison(needle, needle_positions, string)
    
    position = max(substrings, key=lambda x: x[1])
    print(sequences[0][position[0]:position[0]+position[1]])
       

if __name__ == '__main__':
    main()
    