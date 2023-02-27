import logging
from typing import TypeVar, Generic

logging.basicConfig(level=logging.INFO)

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: logging.Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value) + " to " + repr(new))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)


def example_1() -> None:
    lv = LoggedVar("string", "example_1", logging.root)
    v: str = lv.get()
    lv.set("string 2")

def example_2() -> None:
    lv = LoggedVar(1, "example_2", logging.root)
    v: int = lv.get()
    lv.set(2)

def example_3() -> None:
    lv = LoggedVar("string", "example_3", logging.root)
    v: str = lv.get()
    lv.set(1)


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
