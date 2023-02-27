# redirect_std_stream

### Задание

Необходимо написать контекстный менеджер
`redirect_std_stream(stream: Literal["stdout", "stderr"], to: io.IOBase) -> None`
**2 способами** (через генератор / через класс -- `redirect_std_stream_gen`
/ `redirect_std_stream_class`). Обернутый им код должен писать не в "stdout"
/ "stderr", а в объект с файловым интерфейсом (аргумент `to`).

Также ответьте на вопрос:
- **Q**: Чем отличается `sys.stdout` от `sys.__stdout__`?
  - **A**: *ваш ответ*

### Примеры

```python
>>> with open("test_file", "w") as f:
>>>    with redirect_std_stream("stdout", f):
>>>        some_func_that_prints_to_stdout()
```
Все, что `some_func_that_prints_to_stdout` выводила бы в stdout теперь содержится
в файле 'test_file'.
