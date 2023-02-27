import time
from unittest.mock import Mock

import pytest

from hw_04 import timeit


def _sleeper(sleep_for):
    time.sleep(sleep_for)


def test_timeit():
    SLEEP = 0.1

    assert timeit(_sleeper)(SLEEP) == pytest.approx(SLEEP, rel=0.4)
    assert timeit()(_sleeper)(SLEEP) == pytest.approx(SLEEP, rel=0.4)
    assert timeit(n=3)(_sleeper)(SLEEP) == pytest.approx(SLEEP, rel=0.4)


def test_n():
    f = Mock()

    timeit(f, n=100)()
    assert f.call_count == 100

    f.reset_mock()

    timeit(n=200)(f)()
    assert f.call_count == 200
