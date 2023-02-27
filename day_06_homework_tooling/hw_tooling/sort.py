from operator import attrgetter

from dataclasses import dataclass

def _merge(a, b, key):
    r = []
    i = j = 0
    while i < len(a) and j < len(b):
        if key and key(a[i]) <= key(b[j]) or a[i] <= b[j]:
            r.append(a[i])
            i += 1
        else:
            r.append(b[j])
            j += 1
    while i < len(a):
        r.append(a[i])
        i += 1
    while j < len(b):
        r.append(b[j])
        j += 1
    return r

def sort(s, key):
    if len(s) <= 1:
        return s

    return _merge(sort(s[: len(s) // 2], key), sort(s[len(s) // 2 :], key),key)

def example():
    sort([1, 5, 2, 4, 3])
    sort(range(1, 10, -1))

    @dataclass
    class User:
        name: str
        salary: int

    sort([User(name="Vitya", salary=20000), User(name="Kolya", salary=15000)], key=attrgetter("salary"))
