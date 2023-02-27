"""

В этом задании вы будете реализовывать builtin примитив enumerate
Посмотрите, что эта функция делает

"""


QUESTIONS = []


# from typing import Sequence, Iterable



class enumerate__iter_next:
    """Напишите enumerate, не используя генераторы"""

    def __init__(self, iterable, start=0):
        # self.iterable = iter(iterable)
        self._iterator = iter(iterable)  # почему надо делать iter?
        self._next_idx = start

    def __iter__(self):
        return self

    # def __next__(self):
    #     self._next_idx += 1
    #     return self._next_idx - 1, next(self._iterator)
    #     return to_return

    def __next__(self):
        to_return = self._next_idx, next(self._iterator)  # почему именно в таком порядке?
        self._next_idx += 1
        return to_return

class enumerate__iter_generator:
    """Напишите enumerate, через класс и используя генератор для __iter__

    Реализуйте решение так, чтобы объект хранил состояние итерации, т.е.

    enumerator = enumerate__iter_generator('abcd')
    for _ in enumerator:
        break

    for _ in enumerator:  # начинает итерации со второй буквы, т.е. 'b'
        ...
    """

    def __init__(self, iterable, start=0):
        self._iterator = iter(iterable)
        self._next_idx = start

    def __iter__(self):
        for val in self._iterator:
            self._next_idx += 1  # Что здесь не так? Делаем несколько итераторов
            yield self._next_idx, val


QUESTIONS.append(
    """
    Какие вещи потребовалось сделать, чтобы хранить передать состояние итерации в генератор?
    """
)


def enumerate__generator(iterable, start=0):
    """Напишите enumerate через генераторную функцию"""

    idx = 0

    for val in iter(iterable):
        idx += 1
        yield idx, val  # важно ли здесь взять итератор?
        # idx += 1



    ...  # CHANGE THIS


QUESTIONS.append(
    """
    Есть ли какое-то различие в семантике напиcанных примитивов?
    """
)
