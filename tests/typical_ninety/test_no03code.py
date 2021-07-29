import pytest

from practice_atcoder.typical_ninety.no03code import question


class Test(object):
    @pytest.mark.parametrize("n,abn,expect", [
        ("3", ["1 2", "2 3"], "3"),
        ("5", ["1 2", "2 3", "3 4", "3 5"], "4"),
        ("10", ["1 2", "1 3", "2 4", "4 5", "4 6", "3 7", "7 8", "8 9", "8 10"], "8"),
        ("31", ["1 2", "1 3", "2 4", "2 5", "3 6", "3 7", "4 8", "4 9", "5 10", "5 11", "6 12", "6 13", "7 14", "7 15",
                "8 16", "8 17", "9 18", "9 19", "10 20", "10 21", "11 22", "11 23", "12 24", "12 25", "13 26", "13 27",
                "14 28", "14 29", "15 30", "15 31"], "9"),
    ])
    def test(self, n, abn, expect):
        assert question(n, abn) == expect
