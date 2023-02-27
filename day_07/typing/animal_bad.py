from datetime import date


class Animal:
    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    def newborn(cls, name: str) -> "Animal":
        return cls(name, date.today())

class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} says woof!")

foo = Dog.newborn("Foo")
foo.bark()
