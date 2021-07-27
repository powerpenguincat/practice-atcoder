import pytest

from practice_atcoder.typical_ninety.no01code import question


class Test(object):
    @pytest.mark.parametrize("nl,k,an,expect", [
        ("7 45", "2", "7 11 16 20 28 34 38", "12"),
        ("3 100", "1", "28 54 81", "46"),
        ("3 100", "2", "28 54 81", "26"),
        ("20 1000", "4", "51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954", "170"),
    ])
    def test(self, nl, k, an, expect):
        assert question(nl, k, an) == expect
