#pytest task_014

import pytest
from .not_best_solution import make_subs, find_longes_prefix, strings_comparison


def test_make_subs():
    assert make_subs('ACGT') == [(0, 4),(1, 4),(2, 4),(3, 4)]


def test_find_longes_prefix():
    assert find_longes_prefix('ACGT', [1, 4], 'GGGGGG', 0, 6) == 1
    assert find_longes_prefix('G', [0, 1], 'GAAAAA', 0, 6) == 1
    assert find_longes_prefix('GDDDA', [4, 5], 'A', 0, 1) == 5


def test_strings_comparison():
    assert strings_comparison('ATACA', [4, 5], 'GATTACA') == 5
    assert strings_comparison('TTTTT', [0, 1], 'GGGGGG') == 0
    