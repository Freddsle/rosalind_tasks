#Inferring mRNA from Protein http://rosalind.info/problems/mrna/
#Run with "python -m task_017.solution_017"


def codon_counter(protein, modulo):
    codons = {'A':4,'R':6,'N':2,'D':2,'C':2,'E':2,'Q':2,'G':4,'H':2,'I':3,'L':6,'K':2,'M':1,'F':2,'P':4,
              'S':6,'T':4,'W':1,'Y':2,'V':4}
    rna_with_stop = 3
    for amino_acid in protein:
        rna_with_stop = rna_with_stop * codons[amino_acid] % modulo

    return rna_with_stop

def main():
    with open("rosalind_mrna.txt", "r") as f:
        protein = f.read().strip('\n')

    modulo = 1000000    
    print(codon_counter(protein, modulo))


if __name__ == '__main__':
    main()