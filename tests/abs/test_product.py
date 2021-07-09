import pytest

from practice_atcoder.abs.product import question


class TestReturnStr(object):
    @pytest.mark.parametrize("ab,expect", [
        ("3 4", "Even"),
        ("1 21", "Odd"),
    ])
    def test_ok(self, ab, expect):
        assert question(ab) == expect
