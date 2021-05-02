#pytest task_014

import pytest
from .solution import make_subs, find_longes_prefix, pairs_comp


def test_make_subs():
    assert make_subs(4) == [[0, 4],[1, 3],[2, 2],[3, 1]]


def test_find_longes_prefix():
    assert find_longes_prefix('AT', 'AAATTTT') == 1
    assert find_longes_prefix('T', 'AAATTTT') == 0
    assert find_longes_prefix('GCCC', 'G') == 1
    assert find_longes_prefix('C', 'T') == 0

def test_pairs_comp():
    sequences = ['GATTACA', 'TAGACCA', 'ATACA']
    assert pairs_comp(subs_pair=7, sequences=sequences, begin=0, length=7, i=1) == 2
