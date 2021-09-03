import abc
from typing import NoReturn

from domain.model.blog import Blog


class BlogIndex(abc.ABC):

    @abc.abstractmethod
    def add(self, blog: Blog) -> NoReturn:
        pass
