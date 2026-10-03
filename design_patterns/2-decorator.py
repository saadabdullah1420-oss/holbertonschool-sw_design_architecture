#!/usr/bin/env python3


class Beverage:
    def cost(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class Coffee(Beverage):
    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    coffee = Coffee()
    print(coffee.description(), coffee.cost())

    milk_coffee = MilkDecorator(Coffee())
    print(milk_coffee.description(), milk_coffee.cost())

    caramel_coffee = CaramelDecorator(
        MilkDecorator(
            SugarDecorator(
                Coffee()
            )
        )
    )
    print(caramel_coffee.description(), caramel_coffee.cost())


if __name__ == "__main__":
    main()
