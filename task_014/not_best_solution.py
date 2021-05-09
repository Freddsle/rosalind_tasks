#now - BEST
#Finding a Shared Motif http://rosalind.info/problems/lcsm/
#Run with "python -m task_014.not_best_solution"
import itertools
from Bio import SeqIO
from my_utils import my_timer


def make_subs(sequence):
    last_position = len(sequence)
    substrings = []
    for i in range(last_position):
        substrings.append((i, last_position))
    return substrings

 
def find_longes_prefix(needle, needle_positions, haystack, begin_haystack, len_haystack):
    for i, j in zip(range(needle_positions[0], needle_positions[1]), 
                    range(begin_haystack, len_haystack)):
        if needle[i] != haystack[j]:
            return i
    return i + 1


def strings_comparison(needle, needle_positions, haystack):
    result = -1
    len_haystack = len(haystack)

    for begin_haystack in range(len_haystack):
        needle_end = find_longes_prefix(needle, 
                                        needle_positions, 
                                        haystack, 
                                        begin_haystack, 
                                        len_haystack)
        result = max(result, needle_end)
        if result == needle_positions[1]:
            break

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
            for j, needle_positions in enumerate(substrings):
                substring_end = strings_comparison(needle, needle_positions, string)
                substrings[j] = (needle_positions[0], substring_end)
    
    position = max(substrings, key=lambda x: x[1] - x[0])
    print(sequences[0][position[0]:position[1]])
       

if __name__ == '__main__':
    main()
    