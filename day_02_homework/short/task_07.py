QUESTIONS = []

"""

Любым удобным способом (генераторная функция, __iter__ + __next__) сделайте итератор, вытаскивающий элементы из списка произвольной вложенности

Считаем, что список может содержать только списки или какие-то значения, которые и должен возвращать итератор при вызове next()
Воспользуйтесь isinstance для проврки типов
Считаем, что в списке нет бесконечной рекурсии, т.е. нет ссылок на самого себя

"""

flatten_list = ...



# НЕ надо переприсваивать!
# просто удалите эту строку и определите функцию с таким же именем!


def flatten_list(nested_list):
    for value in nested_list:
        if isinstance(value, list):  # не надо проверять iterable
            yield from nested_list(value)
        else:
            yield value