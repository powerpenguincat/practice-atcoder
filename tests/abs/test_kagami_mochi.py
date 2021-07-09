import pytest

from practice_atcoder.abs.kagami_mochi import question


class Test(object):
    @pytest.mark.parametrize("n,dn,expect", [
        ("4", ["10", "8", "8", "6"], "3"),
        ("3", ["15", "15", "15"], "1"),
        ("7", ["50", "30", "50", "100", "50", "80", "30"], "4"),
    ])
    def test(self, n, dn, expect):
        assert question(n, dn) == expect
