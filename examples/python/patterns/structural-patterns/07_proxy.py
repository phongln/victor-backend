from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print('Real Subject handle request')


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._realsubject = real_subject or RealSubject()

    def request(self):
        if self.check_access():
            self._realsubject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")


def client_code(subject: Subject):
    subject.request()


if __name__ == '__main__':
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
