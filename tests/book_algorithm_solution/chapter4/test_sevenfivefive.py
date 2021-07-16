import pytest

from practice_atcoder.book_algorithm_solution.chapter4.sevenfivefive import question


# AtCoder Beginner Contest 114 C - 775.

class Test(object):
    @pytest.mark.parametrize("n,expect", [
        ("575", "4"),
        ("3600", "13"),
        ("999999999", "26484")
    ])
    def test(self, n, expect):
        assert question(n) == expect
