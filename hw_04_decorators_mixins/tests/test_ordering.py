import operator

import pytest

from hw_04 import WithOrderMixin, with_order


class TupleWrapper:
    def __init__(self, *args):
        self._args = args

    def __eq__(self, rhs):
        if not isinstance(rhs, TupleWrapper):
            return NotImplemented
        return self._args == rhs._args

    def __lt__(self, rhs):
        if not isinstance(rhs, TupleWrapper):
            return NotImplemented
        return self._args < rhs._args


class WithMixin(TupleWrapper, WithOrderMixin):
    pass


@with_order
class WithDecorator(TupleWrapper):
    pass


class TestEverything:
    def test_not_implemented(self):
        class Foo(WithOrderMixin):
            pass

        with pytest.raises(TypeError):
            obj = Foo()

    @pytest.mark.parametrize("l_name", [1, 2])
    @pytest.mark.parametrize("l_surname", [1, 2])
    @pytest.mark.parametrize("r_name", [1, 2])
    @pytest.mark.parametrize("r_surname", [1, 2])
    @pytest.mark.parametrize(
        "op", ["__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__"]
    )
    @pytest.mark.parametrize("cls", [WithMixin, WithDecorator])
    def test_bla(self, l_name, l_surname, r_name, r_surname, op, cls):

        lhs = cls(l_name, l_surname)
        rhs = cls(r_name, r_surname)
        op_f = getattr(operator, op)
        assert op_f(lhs, rhs) == op_f(
            (l_name, l_surname),
            (r_name, r_surname),
        )


def test_sdf():
    from functools import total_ordering

    assert total_ordering is not with_order
