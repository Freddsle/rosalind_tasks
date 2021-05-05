import pytest
import re
from .solution016 import find_glycosylation_motif, download_sequences


def test_find_glycosylation_motif():
    with open("long_string.txt", "r") as f:
        sequence = f.read().replace('\n','')
    MOTIF_RE = re.compile(r'(?=(N[^P][S,T][^P]))')
    assert find_glycosylation_motif(sequence, MOTIF_RE) == [84, 117, 141, 305, 394]
    assert find_glycosylation_motif('sequence', MOTIF_RE) == []
    assert find_glycosylation_motif('', MOTIF_RE) == []
    assert find_glycosylation_motif('NNTSHSHL', MOTIF_RE) == [0, 1]


def test_download_sequences():
    accessions_one = ['A2Z669']
    accessions_two = ['']
    assert download_sequences(accessions_one) == {'A2Z669': 'MRASRPVVHPVEAPPPAALAVAAAAVAVEAGVGAGGGAAAHGGENAQPRGVRMKDPPGAPGTPGGLGLRLVQAFFAAAALAVMASTDDFPSVSAFCYLVAAAILQCLWSLSLAVVDIYALLVKRSLRNPQAVCIFTIGDGITGTLTLGAACASAGITVLIGNDLNICANNHCASFETATAMAFISWFALAPSCVLNFWSMASR'}
    try:
        assert download_sequences(accessions_two)
    except ValueError:
        pass