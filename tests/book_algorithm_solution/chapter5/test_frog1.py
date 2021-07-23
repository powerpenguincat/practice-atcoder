import pytest

from practice_atcoder.book_algorithm_solution.chapter5.frog1 import question


# AtCoder Educational DP Contest A - Frog1.
class Test(object):
    @pytest.mark.parametrize("n,hn,expect", [
        ("4", "10 30 40 20", "30"),
        ("2", "10 10", "0"),
        ("6", "30 10 60 10 60 50", "40")
    ])
    def test(self, n, hn, expect):
        assert question(n, hn) == expect
