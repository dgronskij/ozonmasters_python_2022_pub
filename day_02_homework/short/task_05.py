"""

Напишите класс, который считает элементы из итерабла. Считаем, что все они могут быть положены в словарь

Бонус, если унаследуетесь от словаря

Эту задачу будем обсуждать на разборе

"""


class MyCounter(dict):
    def __init__(self, iterable=None):
        if iterable:
            self.extend(iterable)

    def extend(self, iterable):
        for value in iterable:
            self[value] = self.get(value, 0) + 1

    def get_stats(self):  # получить словарь со счетчиками
        return self


# from collections import Counter

# c = Counter('abcdef')

# c.extend(Counter())
