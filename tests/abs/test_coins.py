import pytest

from practice_atcoder.abs.coins import question


class Test(object):
    @pytest.mark.parametrize("a,b,c,x,expect", [
        ("2", "2", "2", "100", "2"),
        ("5", "1", "0", "150", "0"),
        ("30", "40", "50", "6000", "213"),
    ])
    def test(self, a, b, c, x, expect):
        assert question(a, b, c, x) == expect
