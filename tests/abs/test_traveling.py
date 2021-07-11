import pytest

from practice_atcoder.abs.traveling import question


class Test(object):
    @pytest.mark.parametrize("n,txyn,expect", [
        ("2", ["3 1 2", "6 1 1"], "Yes"),
        ("1", ["2 100 100"], "No"),
        ("2", ["5 1 1", "100 1 1"], "No"),
    ])
    def test(self, n, txyn, expect):
        assert question(n, txyn) == expect
