import textwrap

import pytest

from . import task_01
from . import task_02
from . import task_03
from . import task_04
from . import task_05
from . import task_06
from . import task_07
from . import task_08
from . import task_09
from . import task_10


class _CommonMixin:
    def test_questions(self):
        missed_questions = []
        questions = getattr(self.MODULE, "QUESTIONS", [])
        for ix, q in enumerate(questions):
            if "ответ:" not in q.lower():
                q_short = textwrap.shorten(q.strip(), width=30)
                missed_questions.append(
                    f"missed question: {self.MODULE.__name__}, idx={ix}, q={q_short}"
                )

        assert not missed_questions, str(missed_questions)


class TestTask01(_CommonMixin):
    MODULE = task_01


class TestTask02(_CommonMixin):
    MODULE = task_02

    @pytest.mark.parametrize(
        "enumerate_type",
        [
            task_02.enumerate__iter_next,
            task_02.enumerate__iter_generator,
            task_02.enumerate__generator,
        ],
    )
    def test_enumerate(self, enumerate_type):
        s = "abcd"
        assert list(enumerate_type("abcd")) == list(enumerate("abcd"))


class TestTask03(_CommonMixin):
    MODULE = task_03

    @pytest.mark.parametrize(
        "range_type",
        [
            task_03.range__iter_next,
            task_03.range__iter_generator,
            task_03.range__generator,
            task_03.range__with_slice,
        ],
    )
    def test_range(self, range_type):
        assert list(range_type(1, 10)) == list(range(1, 10))

    def test_range_slice(self):
        assert list(task_03.range__with_slice[:10]) == list(range(10))


class TestTask04(_CommonMixin):
    MODULE = task_04

    def test_04(self):
        should_be = dict(a=0, b=1, c=2, d=3)
        assert task_04.inverted_index_comprehension == should_be
        assert task_04.inverted_index_no_comprehension == should_be


class TestTask05(_CommonMixin):
    MODULE = task_05

    def test_counter(self):
        MyCounter = task_05.MyCounter
        assert MyCounter("aba").get_stats() == dict(a=2, b=1)
        assert MyCounter().get_stats() == {}

        c = MyCounter()
        c.extend("aba")
        assert c.get_stats() == dict(a=2, b=1)


class TestTask06(_CommonMixin):
    MODULE = task_06


class TestTask07(_CommonMixin):
    MODULE = task_07

    def test_flatten_list(self):
        assert list(task_07.flatten_list([[[[[[[[1]]], 2], [3, 4]]]], 5])) == [
            1,
            2,
            3,
            4,
            5,
        ]


class TestTask08(_CommonMixin):
    MODULE = task_08

    def test_flatten_dict(self):
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

        assert list(task_08.flatten_dict(d)) == [
            ("item.features.quantiles.0.q50", 20),
            ("item.features.quantiles.1.q100", 40),
            ("item.0", "hello"),
        ]


class TestTask09(_CommonMixin):
    MODULE = task_09

    @pytest.mark.parametrize(
        "cat",
        [
            MODULE.cat_chain,
            MODULE.cat_chain_from_iterable,
        ],
    )
    def test_cat(self, cat, tmp_path):

        p = tmp_path / "input.txt"
        p.write_text("1\n2")

        assert list(cat(p.resolve(), p.resolve())) == ["1\n", "2", "1\n", "2"]


class TestTask10(_CommonMixin):
    MODULE = task_10

    def test_zip(self):
        assert list(self.MODULE.my_zip(range(100500), "ab")) == [(0, "a"), (1, "b")]

    def test_transpose(self):
        rows = [
            list("123"),
            list("456"),
        ]

        should_be = [
            list("14"),
            list("25"),
            list("36"),
        ]

        assert self.MODULE.transpose(rows) == should_be
