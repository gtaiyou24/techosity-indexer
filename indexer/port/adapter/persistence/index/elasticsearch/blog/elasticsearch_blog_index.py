from typing import NoReturn

from elasticsearch import Elasticsearch

from domain.model.blog import BlogIndex, Blog
from logger import log


class ElasticSearchBlogIndex(BlogIndex):
    INDEX_NAME = 'blogs'
    MAPPING = {
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "description": {"type": "text"}
            }
        }
    }

    def __init__(self):
        self.__client = Elasticsearch('elasticsearch')

        # インデックスの存在確認
        if not self.__client.indices.exists(index=self.INDEX_NAME):
            # インデックスを作成
            self.__client.indices.create(index=self.INDEX_NAME, body=self.MAPPING)

    def add(self, blog: Blog) -> NoReturn:
        log.debug("blogをElasticSearchに保存します")
        # ドキュメントの登録
        result = self.__client.create(index=self.INDEX_NAME,
                                      id=blog.id(),
                                      body={"title": blog.title(), "description": blog.description()})
        log.debug("{}".format(result))
