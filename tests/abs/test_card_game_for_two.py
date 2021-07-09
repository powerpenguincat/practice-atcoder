import pytest

from practice_atcoder.abs.card_game_for_two import question


class Test(object):
    @pytest.mark.parametrize("n,an,expect", [
        ("2", "3 1", "2"),
        ("3", "2 7 4", "5"),
        ("4", "20 18 2 18", "18"),
    ])
    def test(self, n, an, expect):
        assert question(n, an) == expect
