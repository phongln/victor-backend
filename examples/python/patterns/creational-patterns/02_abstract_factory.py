from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class ConcreteCreator1(Creator):
    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()


class ConcreteCreator2(Creator):
    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()


class ProductA(ABC):
    @abstractmethod
    def useful_method_a(self) -> str:
        pass


class ConcreteProductA1(ProductA):
    def useful_method_a(self):
        return 'this is description for product A1'


class ConcreteProductA2(ProductA):
    def useful_method_a(self):
        return 'this is description for product A2'


class ProductB(ABC):
    @abstractmethod
    def useful_method_b(self):
        pass

    @abstractmethod
    def something_operation(self):
        pass


class ConcreteProductB1(ProductB):
    def useful_method_b(self):
        return 'Product B1 will be processed'

    def something_operation(self):
        return '{something to operate product B}'


class ConcreteProductB2(ProductB):
    def useful_method_b(self):
        return 'Product B2. Hehe'

    def something_operation(self):
        return 'Product B2. Other operation'


def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.useful_method_a())
    print(product_b.useful_method_b())


if __name__ == '__main__':
    client_code(ConcreteCreator1())
    client_code(ConcreteCreator2())
