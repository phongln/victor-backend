from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context(ABC):
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def operation(self):
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(','.join(result))


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List):
        return reversed(sorted(data))


if __name__ == '__main__':
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.operation()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.operation()
