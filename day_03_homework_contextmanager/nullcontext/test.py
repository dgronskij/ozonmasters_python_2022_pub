import pytest

from .your_code import nullcontext as nc


class MyException(Exception):
    pass


def test_noargs():
    with nc() as value:
        assert value is None


def test_withargs():
    enter_result = object()
    with nc(enter_result=enter_result) as value:
        assert value is enter_result


def test_exception_propagation():
    with pytest.raises(MyException):
        with nc():
            raise MyException("this exception should not be blocked with nullcontext")
