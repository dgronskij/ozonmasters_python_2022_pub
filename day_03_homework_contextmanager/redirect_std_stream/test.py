import io
import sys

import pytest

from .your_code import redirect_std_stream_class, redirect_std_stream_gen


@pytest.mark.parametrize(
    "cm",
    [
        redirect_std_stream_gen,
        redirect_std_stream_class,
    ],
)
class Test:
    def test_stdout(self, cm):
        to = io.StringIO()
        streams_before = [sys.stdout, sys.stderr]
        with cm("stdout", to):
            print("Should be redirected")
        assert streams_before == [sys.stdout, sys.stderr]

        to.flush()
        to.seek(0)
        assert to.read() == "Should be redirected\n"

    def test_stderr(self, cm):
        to = io.StringIO()
        streams_before = [sys.stdout, sys.stderr]
        with cm("stderr", to):
            print("Should be redirected", file=sys.stderr)
        assert streams_before == [sys.stdout, sys.stderr]

        to.flush()
        to.seek(0)
        assert to.read() == "Should be redirected\n"
