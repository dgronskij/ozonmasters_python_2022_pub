import pytest


@pytest.fixture(autouse=True, scope="session")
def database():
    # e.g. SQLite
    print("\nsetup db")
    yield
    print("\nteardown db")


@pytest.fixture(autouse=True, scope="module")
def database_schema():
    print("\nsetup db schema")
    yield
    print("\nteardown db schema")
