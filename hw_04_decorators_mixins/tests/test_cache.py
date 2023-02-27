from unittest.mock import Mock, call

import pytest

from hw_04 import cache


def concrete_func(a, b):
    return a, b


@pytest.fixture
def m():
    """
    This is a fixture providing a mock, wrapping the `concrete_func`
    """
    yield Mock(wraps=concrete_func)


@pytest.fixture
def c(m):
    """
    This is a fixture providing cached `concrete_func`
    """
    yield cache(m)


def test_simple(m, c):
    assert c(1, 2) == (1, 2)  # function called
    assert c(1, 2) == (1, 2)  # cache is used, function is not called
    assert m.call_count == 1


def test_identity(m, c):
    obj = object()
    m.return_value = obj

    assert c(1, 2) is obj  # function called
    assert c(1, 2) is obj  # cache is used, function is not called
    assert m.call_count == 1


def test_kwarg_order(m, c):
    """
    Order of kwargs matters
    """
    c(a=1, b=2)
    c(b=2, a=1)

    assert m.call_count == 1


def test_args_kwargs(m, c):
    """
    Although function is called with the same arguments set,
    from cache perspective they are different
    """
    c(1, 2)
    c(1, b=2)

    assert m.call_count == 2


def test_unique_encoding(m, c):
    """
    This test guards against some wrong and common way to encode arguments into the key
    """

    # all these invocations should have different cache keys!
    invocations = [
        c(1, 2),
        c("1", 2),
        c(1, b=2),
        c(1, "b=2"),
        c(1, "b='2'"),
        c(1, 'b="2"'),
        c(1, ("b", 2)),
        c(1, "b", 2),
    ]

    assert m.call_count == len(invocations)


def test_reset(m, c):
    c(1, 2)
    assert m.call_count == 1

    c.reset()

    c(1, 2)
    assert m.call_count == 2


def test_generic_signature():
    """
    This test checks that any args and kwargs are correcly passed to the
    underlying function
    """

    def generic_func(*args, **kwargs):
        return None

    m = Mock(wraps=generic_func)
    c = cache(m)

    args = tuple("abcdef")
    kwargs = {c: i for i, c in enumerate("xyz")}

    c(*args, **kwargs)
    assert m.call_args == call(*args, **kwargs)


def test_cache_scope(m):
    """
    This test checks that each invokation of `cache` would create a separate cache
    """

    c1 = cache(m)
    c2 = cache(m)

    c1(1, 2)
    assert m.call_count == 1

    c2(1, 2)
    assert m.call_count == 2
