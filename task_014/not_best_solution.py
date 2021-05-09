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
    for i, j in zip(range(needle_positions[0], needle_positions[0] + needle_positions[1]), 
                    range(begin_haystack, len_haystack)):
        if needle[i] != haystack[j]:
            return i - needle_positions[0]
    return i - needle_positions[0] + 1


def strings_comparison(needle, needle_positions, haystack):
    result = -1
    len_haystack = len(haystack)

    for begin_haystack in range(len_haystack):
        length = find_longes_prefix(needle, 
                                    needle_positions, 
                                    haystack, 
                                    begin_haystack, 
                                    len_haystack)
        result = max(result, length)

    return result


@my_timer
def main():
    records = list(SeqIO.parse("rosalind_lcsm.txt", "fasta"))
    # records = list(SeqIO.parse("dna.txt", "fasta"))
    sequences = sorted([record.seq for record in records], key=len)
    
    substrings = make_subs(sequences[0])
    needle = sequences[0]

    for i, string in enumerate(sequences):
        if i > 1:
            for needle_positions in substrings:
                needle_positions[1] = strings_comparison(needle, needle_positions, string)
    
    position = max(substrings, key=lambda x: x[1])
    print(sequences[0][position[0]:position[0]+position[1]])
       

if __name__ == '__main__':
    main()
    