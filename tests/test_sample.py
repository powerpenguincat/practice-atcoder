import pytest

from practice_atcoder.sample import return_str, return_int, return_bool


class TestReturnStr(object):
    @pytest.mark.parametrize("param,expect", [
        ("hoge", "hoge"),
        ("fuga", "fuga"),
        ("piyo", "piyo"),
    ])
    def test_ok(self, param, expect):
        assert return_str(param) == expect

    @pytest.mark.parametrize("param,expect", [
        ("hoge", "fuga"),
        ("fuga", "piyo"),
        ("piyo", "hoge"),
    ])
    def test_ng(self, param, expect):
        assert not return_str(param) == expect


class TestReturnInt(object):
    @pytest.mark.parametrize("param,expect", [
        (1, 1),
        (0, 0),
        (-1, -1),
    ])
    def test_ok(self, param, expect):
        assert return_int(param) == expect

    @pytest.mark.parametrize("param,expect", [
        (1, 2),
        (0, 10),
        (-1, -2),
    ])
    def test_ng(self, param, expect):
        assert not return_int(param) == expect


class TestReturnBool(object):
    @pytest.mark.parametrize("param", [
        True,
    ])
    def test_ok(self, param):
        assert return_bool(param)

    @pytest.mark.parametrize("param", [
        False,
    ])
    def test_ng(self, param):
        assert not return_bool(param)

