from typing import NoReturn

from injector import singleton, inject

from application.command import SaveBlogCommand
from domain.model.blog import BlogRepository, Blog, BlogIndex


@singleton
class SaveBlogApplicationService:
    @inject
    def __init__(self,
                 blog_repository: BlogRepository,
                 blog_index: BlogIndex):
        self.__blog_repository = blog_repository
        self.__blog_index = blog_index

    def save(self, save_blog_command: SaveBlogCommand) -> NoReturn:
        blog = Blog()
        self.__blog_repository.save(blog)
        self.__blog_index.add(blog)
