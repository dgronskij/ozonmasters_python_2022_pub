import pytest

from hw_04 import AttrDict


@pytest.fixture
def d():
    return AttrDict()


def test_set_get_del_attr(d):
    d.a = 10
    assert d.a == 10
    del d.a
    assert d.a != 10


def test_set_get_del_nested_attrs(d):
    d.a.b.c = 10
    assert d.a.b.c == 10
    del d.a.b.c
    assert d.a.b.c != 10


def test_set_multiple_attrs(d):
    d.a = 10
    d.b.c = 20
    d.b.d = 30
    d.b.e.f = 40
    assert d.a == 10
    assert d.b.c == 20
    assert d.b.d == 30
    assert d.b.e.f == 40


def test_del_and_set(d):
    d.a.b = 10
    del d.a.b
    d.a.b.c = 10
