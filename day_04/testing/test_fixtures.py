import pytest


class TestUserDatabase1:
    """ setup_method - teardown_method way
    """
    def setup_method(self, test_method):
        print("\nsetup_method")
        self.user = "USER"

    def teardown_method(self, test_method):
        print("\nteardown_method")
        del self.user

    def test_something1(self):
        assert self.user == "USER"

    def test_something2(self):
        assert self.user == "USER"


"""
Selling points:
* fixtures have explicit names and are activated by declaring their use from
    test functions, modules, classes or whole projects.
* fixtures are implemented in a modular manner, as each fixture name triggers
    a fixture function which can itself use other fixtures.
* fixture management scales from simple unit to complex functional testing,
    allowing to parametrize fixtures and tests according to configuration and
    component options, or to re-use fixtures across function, class, module
    or whole test session scopes.
* teardown logic can be easily, and safely managed, no matter how many
    fixtures are used, without the need to carefully handle errors by hand
    or micromanage the order that cleanup steps are added.
"""


@pytest.fixture
def db_user():
    print("\ncreate user")
    yield "USER"
    print("\nremove user")


class TestUserDatabase2:
    # запрашиваем fixture и получаем yielded значение
    def test_something(self, db_user):
        assert db_user == "USER"


@pytest.fixture
def db_group():
    print("\ncreate group")
    yield "GROUP"
    print("\nremove group")


@pytest.fixture
def db_user_with_group(db_group):
    print("\ncreate user")
    yield "USER"
    print("\nremove user")


class TestUserDatabase3:
    # запрашиваем fixture и получаем yielded значение
    def test_something(self, db_user_with_group):
        assert db_user_with_group == "USER"


@pytest.fixture
def fixture_with_error():
    raise Exception


class TestFoo:
    def test_something(self, fixture_with_error):
        pass


"""
Fixture instantiation order:

Three factors:
* scope
* dependencies
* autouse

Rules:
* Higher-scoped fixtures are executed first
* Fixtures of the same order execute based on dependencies
* Autouse fixtures are executed first within their scope
"""
