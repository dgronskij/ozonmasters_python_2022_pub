import pytest

from unittest.mock import ANY

from typing import ContextManager, Dict, Type


from .your_code import popped_key_class, popped_key_gen


@pytest.fixture()
def d():
    return dict(a=1, b=2, c=3)


class _CasesMixin:
    popped_key: Type[ContextManager[Dict]]

    def test_identity(self, d: Dict):
        with self.popped_key(d, "a") as new_d:
            assert d is new_d, "You have returned another object"

    @pytest.mark.parametrize("key", list("abc"))
    def test_key(self, d, key):
        d_copy = d.copy()
        with self.popped_key(d, key) as new_d:
            assert d_copy == {key: ANY, **new_d}
        assert d_copy == d

    def test_key_error(self, d):
        with pytest.raises(KeyError):
            with self.popped_key(d, "never_existing_key"):
                pass


class TestClass(_CasesMixin):
    popped_key = staticmethod(popped_key_class)


class TestGen(_CasesMixin):
    popped_key = staticmethod(popped_key_gen)
