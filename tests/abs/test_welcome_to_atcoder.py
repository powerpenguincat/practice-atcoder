import pytest

from practice_atcoder.abs.welcome_to_atcoder import question


class TestReturnStr(object):
    @pytest.mark.parametrize("a,bc,s,expect", [
        ("1", "2 3", "test", "6 test"),
        ("72", "128 256", "myonmyon", "456 myonmyon"),
    ])
    def test_ok(self, a, bc, s, expect):
        assert question(a, bc, s) == expect
