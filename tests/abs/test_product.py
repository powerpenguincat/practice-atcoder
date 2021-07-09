import pytest

from practice_atcoder.abs.product import question


class Test(object):
    @pytest.mark.parametrize("ab,expect", [
        ("3 4", "Even"),
        ("1 21", "Odd"),
    ])
    def test(self, ab, expect):
        assert question(ab) == expect
