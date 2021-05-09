#pytest task_017
import pytest
from .solution_017 import codon_counter


def test_codon_counter():
    assert codon_counter('MA', 1000000) == 12
    assert codon_counter('M', 1000000) == 3