QUESTIONS = []

"""

Иногда бывает необходимо развернуть словарь в плоскую структуру.

Любым удобным способом (генераторная функция, __iter__ + __next__) сделайте итератор, вытаскивающий пары

(путь, значение), где
- путь -- "путь" до "значения" в словаре в нотации key1.key2.key3, например,
  из словаря

   d = {
            "item": {
                "features": {
                    "quantiles": [
                        {"q50": 20},
                        {"q100": 40},
                    ]
                },
                0: "hello",
            }
        }

    получаются такие пары

        ("item.features.quantiles.0.q50", 20),
        ("item.features.quantiles.1.q100", 40),
        ("item.0", "hello"),

  Считаем, что в исходном словаре могут быть словари, списки и другие значения, которые и должен возвращать итератор при вызове next()
  Воспользуйтесь isinstance для проврки типов

"""

flatten_dict = ...