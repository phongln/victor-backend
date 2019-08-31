from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()

        return product

    def produce_part_a(self):
        return self._product.add('Product A1')

    def produce_part_b(self):
        return self._product.add('Product B1')

    def produce_part_c(self):
        return self._product.add('Product C1')


class Product1():
    def __init__(self):
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self):
        print(f'{", ".join(self.parts)}\n', end='')


class Director():
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> None:
        return self._builder

    @builder.setter
    def builder(self, buidler):
        self._builder = builder

    def build_minimal(self) -> None:
        self.builder.produce_part_a()

    def build_full(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == '__main__':
    director = Director()
    builder = ConcreteBuilder1()

    director.builder = builder
    director.build_minimal()
    builder.product.list_parts()

    director.build_full()
    builder.product.list_parts()

    # custom builder
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
