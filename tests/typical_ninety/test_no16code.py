import pytest

from practice_atcoder.typical_ninety.no16code import question


class Test(object):
    @pytest.mark.parametrize("n,abc,expect", [
        ("227", "21 47 56", "5"),
        ("9999", "1 5 10", "1004"),
        ("998244353", "314159 265358 97932", "3333"),
        ("100000000", "10001 10002 10003", "9998"),
    ])
    def test(self, n, abc, expect):
        assert question(n, abc) == expect
