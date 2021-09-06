from typing import Type

from injector import Injector, T

from di import DI
from domain.model.blog import BlogIndex
from port.adapter.persistence.index.elasticsearch.blog import ElasticSearchBlogIndex
from port.adapter.persistence.index.inmemory.blog import InMemoryBlogIndex


class DIManager:
    def __init__(self):
        self.__injector = Injector([
            DI.new(BlogIndex, {'elasticsearch': ElasticSearchBlogIndex, 'inmemory': InMemoryBlogIndex})
        ])

    def get(self, interface: Type[T]) -> T:
        return self.__injector.get(interface)
