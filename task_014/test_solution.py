#pytest task_014

import pytest
from .solution import make_subs, find_longes_prefix, strings_comparison


def test_make_subs():
    assert make_subs('ATGCAC') == ['ATGCAC', 'TGCAC', 'GCAC', 'CAC', 'AC', 'C']
    assert make_subs('A') == ['A']


def test_find_longes_prefix():
    assert find_longes_prefix('AT', 'AAATTTT', 1, 7) == 1
    assert find_longes_prefix('T', 'AAATTTT', 0, 7) == 0
    assert find_longes_prefix('GCCC', 'GGGGGG', 0, 6) == 1
    assert find_longes_prefix('C', 'TAAAAAA', 0, 7) == 0


def test_strings_comparison():
    assert sorted(strings_comparison(['ATACA', 'TACA', 'ACA', 'CA', 'A'], 
                                        'TAGACCA'), key=len) == ['A', 'TA', 'CA', 'ACA', 'ATACA']
                                        