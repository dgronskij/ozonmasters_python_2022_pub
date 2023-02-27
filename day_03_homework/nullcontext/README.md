# nullcontext

## Зачем надо
Иногда интерфейс функции ожидает на вход некий контекстный менеджер:

```python

from typing import ContextManager

class FooType:
    pass

def i_require_context_manager(cm: ContextManager[FooType]):
    foo_value: FooType
    with cm as foo_value:
        ...
```

Что делать, если у нас уже есть значение типа `FooType`, которое нужно просто "обернуть"?

## Зачем надо -- 2

Или, что тоже самое, необходимо условно скомбинировать владеющее и не владеющее поведение, инкапуслированное в КМ:

```python

def process_file(file_or_path: Union[str, pathlib.Path, IO]):
    if isinstance(file_or_path, (str, pathlib.Path)):
        file = open(file_or_path)
    else:
        # нам прилетел открытый файл
        file = file_or_path # PROBLEM

    with file:
        # что-то делаем с файлом
```

- **Q: Как вы думаете, почему делать так, как сделано на строке "PROBLEM" -- плохо?**
    - **ОТВЕТ:**
- **Q: Как nullcontext решает проблему выше?**
    - **ОТВЕТ:**



## Что надо сделать

Любым удобным способом (класс, генератор + `@contextmanager`) реализуйте контекстный менеджер `nullcontext(enter_result=None)`, который принимает единственный необязательный аргумент, который и возращает при открытии менеджера


