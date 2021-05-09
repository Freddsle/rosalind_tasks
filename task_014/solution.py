#Finding a Shared Motif http://rosalind.info/problems/lcsm/
#Run with "python -m task_014.solution"
import itertools
import sys
from Bio import SeqIO
from my_utils import my_timer


def make_subs(sequence):
    substrings = [sequence]
    for i in range(len(sequence) - 1):
        substrings.append(substrings[-1][1:])
    return substrings

    
def find_longes_prefix(template_string, haystack, begin, haystack_len):
    for i, letter_template in enumerate(template_string):
        if haystack_len > begin+i:
            if letter_template != haystack[begin+i]:
                return i
        else:
            return i
    return i + 1


def strings_comparison(needle, haystack):
    for c, template_string in enumerate(needle):
        last_pos = []
        haystack_len = len(haystack)
        new_needle = needle
        for begin in range(haystack_len):
            last_pos.append(find_longes_prefix(template_string, haystack, begin, haystack_len))
        new_needle[c] = template_string[:max(last_pos)]
    return [a[0] for a in itertools.groupby(sorted(new_needle))]


@my_timer
def main():
    # records = list(SeqIO.parse("rosalind_lcsm.txt", "fasta"))
    records = list(SeqIO.parse("dna.txt", "fasta"))
    sequences = sorted([record.seq for record in records], key=len)
    for i, string in enumerate(sequences):
        if i == 0:
            needle = make_subs(sequences[0])
        else:
            needle = strings_comparison(needle, string)
    print(max(needle, key=len))
       

if __name__ == '__main__':
    main()