from __future__ import annotations
from typing import Optional


class SingletonMeta(type):
    _instance: Optional[Singleton] = None

    def __call__(self) -> Singleton:
        if self._instance is None:
            self._instance = super().__call__()

        return self._instance


class Singleton(metaclass=SingletonMeta):
    def some_operation(self):
        pass


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
