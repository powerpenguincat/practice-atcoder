import pytest

from practice_atcoder.book_algorithm_solution.chapter3.sum_of_three_integers import question


# AtCoder Beginner Contest 051 B - Sum of Three Integers.
class Test(object):
    @pytest.mark.parametrize("ks,expect", [
        ("2 2", "6"),
        ("5 15", "1")
    ])
    def test(self, ks, expect):
        assert question(ks) == expect
