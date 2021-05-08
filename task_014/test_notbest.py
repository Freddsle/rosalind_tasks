#pytest task_014

import pytest
from .not_best_solution import make_subs, find_longes_prefix, strings_comparison


def test_make_subs():
    assert make_subs('ACGT') == [[0, 4],[1, 3],[2, 2],[3, 1]]


def test_find_longes_prefix():
    assert find_longes_prefix('ACGT', [1, 3], 'GGGGGG', 0, 6) == 0
    assert find_longes_prefix('G', [0, 1], 'GAAAAA', 0, 6) == 1
    assert find_longes_prefix('GDDDA', [4, 1], 'A', 0, 1) == 1


def test_strings_comparison():
    assert strings_comparison('ATACA', [4, 1], 'GATTACA') == 1
    assert strings_comparison('TTTTT', [0, 1], 'GGGGGG') == 0
    