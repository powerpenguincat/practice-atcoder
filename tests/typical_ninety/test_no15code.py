import pytest

from practice_atcoder.typical_ninety.no15code import question


class Test(object):
    @pytest.mark.parametrize("n,expect", [
        ("1", ["1"]),
        ("2", ["3", "2"]),
        ("3", ["7", "4", "3"]),
        ("4", ["15", "7", "5", "4"]),
        ("7", ["127", "33", "18", "13", "10", "8", "7"]),
    ])
    def test(self, n, expect):
        assert question(n) == expect
