from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observers: List(Observer) = []

    def attach(self, observer: Observer):
        print(f'Add new observer to list')
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def operation(self):
        self._state = randrange(10)
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass


class ConcreteObserverA(Observer):
    def update(self, subject):
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == '__main__':
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.operation()
    subject.operation()

    subject.detach(observer_a)
    subject.operation
