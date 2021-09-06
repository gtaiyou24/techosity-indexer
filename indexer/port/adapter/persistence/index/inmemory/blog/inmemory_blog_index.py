from typing import NoReturn

from domain.model.blog import BlogIndex, Blog


class InMemoryBlogIndex(BlogIndex):

    def __init__(self):
        self.__blogs = dict()

    def add(self, blog: Blog) -> NoReturn:
        self.__blogs[blog.id()] = blog
