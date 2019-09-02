from __future__ import annotations


class Facade():
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1():
    def operation1(self):
        return "Subsystem1: Ready!"

    def operation_n(self):
        return "Subsystem1: Go!"


class Subsystem2():
    def operation1(self):
        return "Subsystem2: Get ready!"

    def operation_z(self):
        return "Subsystem2: Fire!"


def client_code(facade: Facade):
    print(facade.operation())


if __name__ == '__main__':
    sub1 = Subsystem1()
    sub2 = Subsystem2()

    facade = Facade(sub1, sub2)
    client_code(facade)
