import pytest
from unittest.mock import Mock

from .your_code import closing, Closable


def test_no_exc():
    handle = Mock(Closable)

    with closing(handle) as value:
        pass

    assert value is None, "closing context manager should return nothgin as a value"
    assert handle.close.call_count == 1


def test_exc():
    handle = Mock(Closable)

    class MyException(Exception):
        pass

    with pytest.raises(MyException):
        with closing(handle):
            raise MyException("this should not be intercepted")

    assert handle.close.call_count == 1
