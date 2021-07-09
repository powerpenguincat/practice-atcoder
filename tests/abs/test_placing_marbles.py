import pytest

from practice_atcoder.abs.placing_marbles import question


class Test(object):
    @pytest.mark.parametrize("sss,expect", [
        ("101", "2"),
        ("000", "0"),
    ])
    def test(self, sss, expect):
        assert question(sss) == expect
