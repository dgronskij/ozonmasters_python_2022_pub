from contextlib import contextmanager
from typing import ContextManager, Dict, Protocol


class Closable(Protocol):
    def close(self) -> None:
        ...


closing = ...  # CHANGE ME
