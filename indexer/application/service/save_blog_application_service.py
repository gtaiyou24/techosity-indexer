from typing import NoReturn

from injector import singleton, inject

from application.command import SaveBlogCommand
from domain.model.blog import Blog, BlogIndex
from logger import log


@singleton
class SaveBlogApplicationService:
    @inject
    def __init__(self, blog_index: BlogIndex):
        self.__blog_index = blog_index

    def save(self, save_blog_command: SaveBlogCommand) -> NoReturn:
        log.debug("CommandからBlogを生成します。")
        blog = Blog.of(
            save_blog_command.blog_id,
            save_blog_command.blog_title,
            save_blog_command.blog_description,
            save_blog_command.url
        )
        log.debug("Blog {} を生成しました".format(blog))

        log.debug("blogを保存します")
        self.__blog_index.add(blog)
