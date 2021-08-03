import pytest

from practice_atcoder.typical_ninety.no08code import question


class Test(object):
    @pytest.mark.parametrize("s,expect", [
        ("attcoderer", "6"),
        ("aattccooddeerr", "128"),
        ("atcoderatcoderatcoderatcoderatcoderatcoderatcoderatcoderatcoder", "6435"),
        ("brckpixvbzptpfobpgwgfnovgjrruladpoapohzyqkmmaapnumhhuuaudztrgnjpwvnggnevmjisvbgoqsvwgozkkmcrydrojxrofvckrgksjnyhqfvbhawzkpddgbyiscopxnxmduanahfhzcnixkpexrcazqetinblpscyqwxkcfcbmpjekklaueoxolxiszagoruxrjewiajmczelvirqobkuiaxmaalkbckwbnbbtyixfjbgltljfdsblrlakktjbwlufsuobzhixzwbmeoethbmpmictanarheouadgjcfhlbrckyzwoqowmvmesqmfdyeomuglutqtbxztvoxtvmqyqqjgqjdkysbvtqdsurgmvctodjqspzgeyuogpadapiibqqjokrmqgiekggmfxxiwyytwyjqgkyefridarszlpazqhezlihscempkddhfhzkqataieopttyuddweukffjgdicqyobvdjnlftibaoqdvgg", "99337"),
    ])
    def test(self, s, expect):
        assert question(s) == expect
