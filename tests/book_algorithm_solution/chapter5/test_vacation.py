import pytest

from practice_atcoder.book_algorithm_solution.chapter5.vacation import question


# AtCoder Educational DP Contest C - Vacation.
class Test(object):
    @pytest.mark.parametrize("n,abcn,expect", [
        ("3", ["10 40 70", "20 50 80", "30 60 90"], "210"),
        ("1", ["100 10 1"], "100"),
        ("7", ["6 7 8", "8 8 3", "2 5 2", "7 8 6", "4 6 8", "2 3 4", "7 5 1"], "46")
    ])
    def test(self, n, abcn, expect):
        assert question(n, abcn) == expect
