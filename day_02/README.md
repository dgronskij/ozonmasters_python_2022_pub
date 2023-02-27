# day_02 :: Лекция / Семинар от 2022-02-17 (Thu)

Говорили про

## Git

- Преимущества и недостатки
- Поговорили про важные настройки в .gitconfig
   - мой можете посмотреть [здесь](https://github.com/dgronskij/dotconfigs/blob/master/git/.gitconfig)
- Что представляет собой под капотом -- blobs -> trees -> commits
- Поэкспериментировали
- Попробовали что-то поделать в Gitlab

[Слайды](./git.pdf)

## YAML

Практически не поговорили.

Почитайте про YAML Anchors [пример для docker compose](https://www.cloudsavvyit.com/10765/how-to-simplify-docker-compose-files-with-yaml-anchors-and-extensions/)

Совершенно не поговорили про грабли:
- https://noyaml.com/
- https://docs.saltproject.io/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html
- https://yaml-multiline.info/

### Совет дня
tl;dr -- используйте кавычки, чтобы избежать незапланированного cast-а к другому типу
В случае сомнений -- переведите yaml в json и посмотрите как оно точно будет интрпретироваться

## Gitlab CI

Поговорили 5 минут, запустили в live режиме пару CI джоб


### Материалы
- https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html
- https://docs.gitlab.com/ee/ci/examples/


## Python -- Iterable / Iterator / Generator

[Jupyter Notebook](./iterator_protocol.ipynb)