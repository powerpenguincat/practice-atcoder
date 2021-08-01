import pytest

from practice_atcoder.typical_ninety.no06code import question


class Test(object):
    @pytest.mark.parametrize("s,k,expect", [
        ("atcoder", "3", "acd"),
        ("competitiveprogramming", "5", "aming"),
        ("competitiveprogramming", "10", "ceegamming"),
        ("competitiveprogramming", "22", "competitiveprogramming"),
    ])
    def test(self, s, k, expect):
        assert question(s, k) == expect
