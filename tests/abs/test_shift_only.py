import pytest

from practice_atcoder.abs.shift_only import question


class Test(object):
    @pytest.mark.parametrize("n,an,expect", [
        ("3", "8 12 40", "2"),
        ("4", "5 6 8 10", "0"),
        ("6", "382253568 723152896 37802240 379425024 404894720 471526144", "8"),
    ])
    def test(self, n, an, expect):
        assert question(n, an) == expect
