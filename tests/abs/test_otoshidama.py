import pandas as pd
import pytest

from practice_atcoder.abs.otoshidama import question


class Test(object):
    csv_file = "tests/abs/test_otoshidama.csv"
    csv_data = list(pd.read_csv(csv_file, sep=", ", quotechar='"', engine="python"))
    answer = map(lambda s: s.replace('"', ''), csv_data)

    @pytest.mark.parametrize("ny,expect", [
        ("9 45000", ['0 9 0', '1 7 0', '2 5 0', '3 3 0', '4 0 5', '4 1 0']),
        ("20 196000", ["-1 -1 -1"]),
        ("1000 1234000", answer),
    ])
    def test(self, ny, expect):
        assert question(ny) in expect
