# popped_key

Напишите **двумя способами** popped_key контекстный менеджер с семинара (те, кто решали задачу "у доски" на семинаре, уже имеют 2 балла за нее)

- **Q: в тесте используется ключевое слово `is`. Чем `is` сравнение отличается от `==`?**
    - **Ответ:**
- **Q: как работает `==` для кастомных типов, если не определить свой `__eq__`?**
    - **Ответ:**
- **Q: В тесте используется `pytest.ANY`. Посмотрите на `assert`, в котором он используется. Объясните физический смысл проверки, котрая там делается и зачем там нужен `ANY`**
    - **Ответ:**

## Формальное описание

```python

d = dict(a=1, b=2)

with popped_key(d, 'a') as value:
    assert value is d
    assert d == dict(b=2)

with popped_key(d, 'b'):
    assert d == dict(a=1)

with poped_key(d, 'c'):  # KeyError
    pass
```
