class Target():
    def request(self) -> str:
        return 'Target: Target behavior'


class Adaptee():
    def specific_request(self) -> str:
        return 'roivaheb eetpadA'


class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def clien_code(target: Target) -> str:
    print(target.request())


if __name__ == '__main__':
    target = Target()
    clien_code(target)

    adaptee = Adaptee()
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    adapter = Adapter(adaptee)
    clien_code(adapter)
