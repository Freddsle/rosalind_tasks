#pytest task_014

import pytest
from .solution import make_subs, find_longes_prefix, strings_comparison


def test_make_subs():
    assert make_subs('ATGCAC') == ['ATGCAC', 'TGCAC', 'GCAC', 'CAC', 'AC', 'C']
    assert make_subs('A') == ['A']


def test_find_longes_prefix():
    assert find_longes_prefix('AT', 'AAATTTT', 7, 1) == 1
    assert find_longes_prefix('T', 'AAATTTT', 7, 0) == 0
    assert find_longes_prefix('GCCC', 'GGGGGG', 6, 0) == 1
    assert find_longes_prefix('C', 'TAAAAAA', 7, 0) == 0


def test_strings_comparison():
    assert strings_comparison(['ATACA', 'TACA', 'ACA', 'CA', 'A'], 'TAGACCA') == ['A', 'ACA', 'ATACA', 'CA', 'TA']
