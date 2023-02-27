"""

В этом задании вы будете реализовывать builtin примитив range
Посмотрите, что эта функция делает и ее API

"""


QUESTIONS = []


class range__iter_next:
    """Напишите range, не используя генераторы"""

    ...  # CHANGE THIS


class range__iter_generator:
    """Напишите range, через класс и используя генераторную функцию для __iter__

    Реализуйте решение так, чтобы объект хранил состояние итерации, т.е.

    enumerator = range(10)
    for _ in enumerator:
        break
    for _ in enumerator:  # начинает итерации со второй позиции, т.е. 1
        ...
    """

    ...  # CHANGE THIS


QUESTIONS.append(
    """
    Какие вещи потребовалось сделать, чтобы передать состояние итерации в генератор?
    """
)


def range__generator(iterable, start=0):
    """Напишите range через генераторную функцию"""

    ...  # CHANGE THIS


"""
Напишите range так, чтобы дополнительно к стандартному синтаксису, работала конструкция

range[:10], другими словами работал метод __getitem__ со slice в качестве аргумента
"""


range__with_slice = ...  # CHANGE THIS

range__with_slice[1:20]  # must return range(1, 20)

# for el in range__with_slice(1, 20)


class range__with_slice__type:
    def __getitem__(self, s):
        if not isinstance(s, slice):
            raise TypeError("Slices only")

        # return range(s.start or 0, s.end, s.step or 1)

    def __call__(self, *args):
        ...
        return range(...)

range__with_slice = range__with_slice__type()
