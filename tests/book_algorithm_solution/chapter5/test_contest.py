import pytest

from practice_atcoder.book_algorithm_solution.chapter5.contest import question


# AtCoder Typical DP Contest A - Contest.
class Test(object):
    @pytest.mark.parametrize("n,pn,expect", [
        ("3", "2 3 5", "7"),
        ("10", "1 1 1 1 1 1 1 1 1 1", "11")
    ])
    def test(self, n, pn, expect):
        assert question(n, pn) == expect
