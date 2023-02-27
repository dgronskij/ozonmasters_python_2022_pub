from unittest.mock import Mock

from .your_code import cm


def test_cm():
    m = Mock()
    for _ in cm(m):
        m.on_enter.assert_called_once_with()
        m.on_exit.assert_not_called()
    m.on_enter.assert_called_once_with()
    m.on_exit.assert_called_once_with()
