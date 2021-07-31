import pytest

from practice_atcoder.typical_ninety.no05code import question


class Test(object):
    @pytest.mark.parametrize("nbk,cn,expect", [
        ("3 7 3", "1 4 9", "3"),
        ("5 2 3", "1 4 9", "81"),
        ("10000 27 7", "1 3 4 6 7 8 9", "989112238"),
        ("1000000000000000000 29 6", "1 2 4 5 7 9", "853993813"),
        ("1000000000000000000 957 7", "1 2 3 5 6 7 9", "205384995"),
    ])
    def test(self, nbk, cn, expect):
        assert question(nbk, cn) == expect
