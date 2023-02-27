import pytest
from typing import Any, Optional, Type, TypeVar, ContextManager

from .your_code import ExitStack


ExcType = Type[Exception]

# fmt: off
class MyException(Exception):  pass
class MyException2(Exception): pass
class MyException3(Exception): pass
# fmt: on


class EventRecorderContextManager(ContextManager):
    def __init__(
        self,
        id: int,
        event_tape: list,
        *,
        enter_return_value: Any = None,
        exit_block_exceptions: bool = False,
        on_enter_exc_type: Optional[ExcType] = None,
        on_exit_exc_type: Optional[ExcType] = None,
    ):
        self._id = id
        self._tape = event_tape
        self._enter_return_value = enter_return_value
        self._exit_block_exceptions = exit_block_exceptions
        self._on_enter_exc_type = on_enter_exc_type
        self._on_exit_exc_type = on_exit_exc_type

    def __enter__(self) -> Any:
        self._tape.append((self._id, "__enter__"))
        if self._on_enter_exc_type:
            raise self._on_enter_exc_type
        return self._enter_return_value

    def __exit__(self, exc_type, *other) -> bool:
        self._tape.append((self._id, "__exit__", exc_type))
        if self._on_exit_exc_type:
            raise self._on_exit_exc_type
        return self._exit_block_exceptions


def test_simple():
    tape = []
    obj = object()
    cm0 = EventRecorderContextManager(0, tape, enter_return_value=obj)

    with ExitStack() as stack:
        value = stack.enter_context(cm0)
        assert value is obj
        assert tape == [
            (0, "__enter__"),
        ]

    assert tape == [
        (0, "__enter__"),
        (0, "__exit__", None),
    ]


def test_simple_exc():
    """
    If context manager raises upon `__enter__`, its `__exit__` should not be called upon
    exit stack unwinding
    """
    tape = []
    cm0 = EventRecorderContextManager(0, tape, on_enter_exc_type=MyException)

    with pytest.raises(MyException):
        with ExitStack() as stack:
            stack.enter_context(cm0)

    assert tape == [
        (0, "__enter__"),
    ]


def test_nested():
    """
    Here we check that exit stack unwinds in stack order, i.e. innter-most context managers
    are closed first
    """
    tape = []
    cm0 = EventRecorderContextManager(0, tape)
    cm1 = EventRecorderContextManager(1, tape)

    with ExitStack() as stack:
        stack.enter_context(cm0)
        stack.enter_context(cm1)
        assert tape == [
            (0, "__enter__"),
            (1, "__enter__"),
        ]

    assert tape == [
        (0, "__enter__"),
        (1, "__enter__"),
        (1, "__exit__", None),
        (0, "__exit__", None),
    ]


def test_nested_exc():
    """
    If, upon stack unwinding, any `__exit__` raises, it's exception is passed to subsequent __exit__-s
    """
    tape = []
    cm0 = EventRecorderContextManager(0, tape, on_exit_exc_type=MyException3)
    cm1 = EventRecorderContextManager(1, tape, on_exit_exc_type=MyException2)

    with pytest.raises(MyException3):
        with ExitStack() as stack:
            stack.enter_context(cm0)
            stack.enter_context(cm1)
            raise MyException

    assert tape == [
        (0, "__enter__"),
        (1, "__enter__"),
        (1, "__exit__", MyException),
        (0, "__exit__", MyException2),
    ]


def test_nested_exc__block_exc():
    """
    Same test, but with blocking
    """
    tape = []
    cm0 = EventRecorderContextManager(0, tape, on_exit_exc_type=MyException3)
    cm1 = EventRecorderContextManager(1, tape, exit_block_exceptions=True)

    with pytest.raises(MyException3):
        with ExitStack() as stack:
            stack.enter_context(cm0)
            stack.enter_context(cm1)
            raise MyException

    assert tape == [
        (0, "__enter__"),
        (1, "__enter__"),
        (1, "__exit__", MyException),
        (0, "__exit__", None),
    ]


def test_nested_exc_on_open():
    """ """
    tape = []
    cm0 = EventRecorderContextManager(0, tape, on_enter_exc_type=MyException3)
    cm1 = EventRecorderContextManager(1, tape, on_exit_exc_type=MyException2)

    with pytest.raises(MyException2):
        with ExitStack() as stack:
            try:
                stack.enter_context(cm0)
            except Exception:
                pass

            stack.enter_context(cm1)
            raise MyException

    assert tape == [
        (0, "__enter__"),
        (1, "__enter__"),
        (1, "__exit__", MyException),
    ]
