import pytest

from practice_atcoder.other.chokudai import question


# AtCoder Beginner Contest 211 C - chokudai.
class Test(object):
    @pytest.mark.parametrize("s,expect", [
        ("chchokudai", "3"),
        ("atcoderrr", "0"),
        ("chokudaichokudaichokudai", "45")
    ])
    def test(self, s, expect):
        assert question(s) == expect
