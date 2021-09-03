import abc
from typing import NoReturn

from domain.model.blog import Blog


class BlogRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, blog: Blog) -> NoReturn:
        pass
