"""

dict можно создать из итерабла пар

Создайте обратный индекс для списка. Используйте enumerate
Cчитайте, что все элементы в списке уникальные.

Напишите два варинта – с dict comprehension и без (с генераторным выражением)

Замените две строчки ниже

inverted_index_comprehension = ...
inverted_index_no_comprehension = ...

"""
QUESTIONS = []

chars_index = list("abcd")

QUESTIONS.append(
    """
    Почему выражение выше работает?
    """
)


inverted_index_comprehension = ...  # CHANGE THIS
inverted_index_no_comprehension = ...  # CHANGE THIS


QUESTIONS.append(
    """
    Что будет, если элементы в списке не уникальные?
    """
)
