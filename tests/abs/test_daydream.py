import pytest

from practice_atcoder.abs.daydream import question


class Test(object):
    @pytest.mark.parametrize("s,expect", [
        ("erasedream", "YES"),
        ("dreameraser", "YES"),
        ("dreamerer", "NO"),
    ])
    def test(self, s, expect):
        assert question(s) == expect
