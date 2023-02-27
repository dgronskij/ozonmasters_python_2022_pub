"""

Напишите гененратор, который построчно конкатенирует текстовые файлы.
Воспользуйтесь тем, что файл -- сам по себе итерабельный объект


- В первом варианте используйте itertools.chain

Сделайте так, чтобы файлы открывались лениво
(т.е. надо написать итерабельный враппер над файлом,
который будет его открывать при попытке итерации)

NB: это всего лишь упражнение, чтобы заставить втиснуться в рамки существующих интерфейсов.
Скорее всего у вас получится не exception-safe код
Поговорим об этом на разборе

- Во втором варианте используйте itertools.chain.from_iterable

"""

from itertools import chain

def LazyFileWrapper(filename):
    with open(filename) as f:
        yield from f

    # yield from open(filename)

def cat_chain(*filenames):

    # chain(*(open(fn) for fn in filenames))
    yield from chain(*(LazyFileWrapper(fn) for fn in filenames))




def cat_chain_from_iterable(*filenames):
    # ...  # CHANGE ME
    yield from chain.from_iterable(LazyFileWrapper(fn) for fn in filenames))
    # yield from chain.from_iterable(open(fn) for fn in filenames)

    # for fn in filenames:
    #     with open(fn) as f:
    #         yield from f
