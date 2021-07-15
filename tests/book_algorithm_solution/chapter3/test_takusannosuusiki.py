import pytest

from practice_atcoder.book_algorithm_solution.chapter3.takusannosuusiki import question


# AtCoder Beginner Contest 051 B - Sum of Three Integers.
class Test(object):
    @pytest.mark.parametrize("s,expect", [
        ("125", "176"),
        ("9999999999", "12656242944")
    ])
    def test(self, s, expect):
        assert question(s) == expect
