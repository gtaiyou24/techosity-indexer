from typing import Type

from injector import Injector, T


class DIManager:
    def __init__(self):
        self.__injector = Injector([])

    def get(self, interface: Type[T]) -> T:
        return self.__injector.get(interface)
