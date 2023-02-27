import pytest

from .your_code import raises_class, raises_gen


@pytest.mark.parametrize(
    "cm",
    [
        raises_gen,
        raises_class,
    ],
)
class Test:
    def test_raise_expected_exc(self, cm):
        with cm(ValueError):
            raise ValueError

    def test_raise_one_of_expected_exc(self, cm):
        with cm((ValueError, ZeroDivisionError)):
            1 / 0

    def test_raise_descendant_exc_of_expected_exc(self, cm):
        """Please, read about exc hierarchy here: https://docs.python.org/3/library/exceptions.html"""
        with cm(ArithmeticError):
            1 / 0

    def test_raise_unexpected_exc(self, cm):
        try:
            with cm(ValueError):
                raise Exception
        except Exception:
            pass
        else:
            raise Exception("test failed")

    def test_not_raise(self, cm):
        try:
            with cm(ValueError):
                pass
        except Exception:
            pass
        else:
            raise Exception("test failed")
