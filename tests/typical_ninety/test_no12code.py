import pytest

from practice_atcoder.typical_ninety.no12code import question


class Test(object):
    @pytest.mark.parametrize("hw,q,qn,expect", [
        ("3 3", "10", ["1 2 2", "1 1 1", "2 1 1 2 2", "1 3 2", "2 1 1 2 2", "2 2 2 3 2", "1 2 3", "1 2 1", "2 1 1 2 2",
                       "2 1 1 3 3"], ["No", "No", "Yes", "Yes", "No"]),
        ("1 1", "3", ["2 1 1 1 1", "1 1 1", "2 1 1 1 1"], ["No", "Yes"]),
    ])
    def test(self, hw, q, qn, expect):
        assert question(hw, q, qn) == expect
