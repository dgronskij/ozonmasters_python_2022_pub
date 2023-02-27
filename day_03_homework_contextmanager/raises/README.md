# raises

### Задание

Необходимо написать контекстный менеджер
`raises(expected_exc: Union[Exception, Tuple[Exception]]) -> None`
**2 способами** (через генератор / через класс -- `raises_gen`
/ `raises_class`), который позволяет проверить, вызвал ли код
*определенное исключение*. Если вызвал, то продолжается выполнение
программы, иначе `raises` вызывает исключение.

### Примеры

```python
>>> with raises(ZeroDivisionError):
>>>    1 / 0
>>> print("Hi")
Hi
```

```python
>>> with raises(ZeroDivisionError):
>>>    pass
>>> print("Hi")
Traceback (most recent call last):
  ...
<Exception Type>: ZeroDivisionError was not raised
```
