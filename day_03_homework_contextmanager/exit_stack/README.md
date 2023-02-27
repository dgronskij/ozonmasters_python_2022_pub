# ExitStack

Напишите

```python
from contextlib import AbstractContextManager
from typing import ContextManager, TypeVar

T = TypeVar("T")

class ExitStack(AbstractContextManager):
    def enter_context(self, cm: ContextManager[T]) -> T:
        ...
```

Который в `enter_context`
- вызывает `cm.__enter__` и пробрасывает возвращенное оттуда значение
- регистрирует вызов `cm.__exit__`, который будет вызван при выходе из ExitStack

Важно:
- Порядок раскрутки `__exit__`-ов -- в порядке стека
- В случае, если `cm.__enter__` кидает исключение -- `cm.__exit__` не регистрируется
- В случае, если `cm.__exit__` кидается исключением, то оно пробрасывается по стеку дальше
- Полный перечень условий см. в тестах


## Зачем нужно

- Самый гибкий способ линамически определять "ленту" ресурсов
- Кол-во контекстных менеджеров может быть заранее не известно (например, список файлов)
