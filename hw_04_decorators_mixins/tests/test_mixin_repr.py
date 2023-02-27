import pytest

from hw_04 import ReprMixin


def _public_only(dct):
    return {k: v for k, v in dct.items() if not k.startswith("_")}


class Foo(ReprMixin):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __eq__(self, rhs):
        if not isinstance(rhs, Foo):
            return NotImplemented

        return _public_only(self.__dict__) == _public_only(rhs.__dict__)


def test_repr():
    foo = Foo(a=1, b="asdasd", c="1")
    assert eval(repr(foo)) == foo
