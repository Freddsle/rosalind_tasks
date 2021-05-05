#Finding a Protein Motif http://rosalind.info/problems/mprt/
from Bio import ExPASy, SwissProt
import re


def download_sequences(accessions):
    records = {}
    for accession in accessions:
        handle = ExPASy.get_sprot_raw(accession)
        record = SwissProt.read(handle)
        records[accession] = record.sequence
    return records


def find_glycosylation_motif(sequence, MOTIF_RE):
    return [m.start() for m in MOTIF_RE.finditer(sequence)]
    

def main():
    # accessions = ['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST']
    with open("rosalind_mprt.txt", "r") as f:
        accessions = f.read().split()
    records = download_sequences(accessions)
    MOTIF_RE = re.compile(r'(?=(N[^P][S,T][^P]))')
    for seq_id in records:
        result = find_glycosylation_motif(records[seq_id], MOTIF_RE)
        if result != []:
            print(seq_id)
            print(*[x+1 for x in result])


if __name__ == '__main__':
    main()   
    