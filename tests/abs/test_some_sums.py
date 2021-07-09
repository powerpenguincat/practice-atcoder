import pytest

from practice_atcoder.abs.some_sums import question


class Test(object):
    @pytest.mark.parametrize("nab,expect", [
        ("20 2 5", "84"),
        ("10 1 2", "13"),
        ("100 4 16", "4554"),
    ])
    def test(self, nab, expect):
        assert question(nab) == expect
