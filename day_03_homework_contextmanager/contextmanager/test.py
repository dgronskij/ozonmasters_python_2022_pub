from .your_code import contextmanager


def test_name_and_docstring():
    @contextmanager
    def cm():
        """This is docstring of original generator!"""
        pass

    assert cm.__name__ == "cm"
    assert cm.__doc__ == "This is docstring of original generator!"


def test_args_kwargs_return():
    @contextmanager
    def cm(a, b, c, d):
        try:
            yield a + b + c + d
        finally:
            pass

    with cm(1, 2, c=3, d=4) as x:
        assert x == 10


def test_simple_case():
    x = 1

    @contextmanager
    def cm():
        nonlocal x
        x += 1
        try:
            yield 100
        finally:
            x += 1

    m = cm()
    assert x == 1
    with m as y:
        assert x == 2
        assert y == 100
    assert x == 3


def test_exception():
    @contextmanager
    def cm():
        try:
            yield
        finally:
            pass

    try:
        with cm():
            raise ValueError
    except ValueError:
        pass
    else:
        raise Exception("Test failed")


def test_catch_exception():
    @contextmanager
    def cm():
        try:
            yield
        except ValueError:
            pass
        finally:
            pass

    with cm():
        raise ValueError


def test_yield_more_than_once():
    @contextmanager
    def cm():
        yield
        yield

    try:
        with cm():
            pass
    except RuntimeError:
        pass
    else:
        raise Exception("Test failed")


def test_yield_more_than_once_raise_exception():
    @contextmanager
    def cm():
        try:
            yield
        except:
            pass
        yield

    try:
        with cm():
            raise ValueError
    except RuntimeError:
        pass
    else:
        raise Exception("Test failed")


def test_did_not_yield():
    @contextmanager
    def cm():
        yield from []

    try:
        with cm():
            pass
    except RuntimeError:
        pass
    else:
        raise Exception("Test failed")


def test_corner_case_with_StopIteration():
    @contextmanager
    def cm():
        try:
            yield
        finally:
            pass

    try:
        with cm():
            raise StopIteration
    except StopIteration:
        pass
    else:
        raise Exception("Test failed")
    try:
        with cm():
            raise RuntimeError
    except RuntimeError:
        pass
    else:
        raise Exception("Test failed")
