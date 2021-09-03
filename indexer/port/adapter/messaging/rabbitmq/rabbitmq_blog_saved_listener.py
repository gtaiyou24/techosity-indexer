import os
from typing import NoReturn

import pika
from injector import inject, singleton

from application.command import SaveBlogCommand
from application.service import SaveBlogApplicationService
from port.adapter.messaging import ExchangeListener


class RabbitMQBlogSavedListener(ExchangeListener):

    @inject
    def __init__(self):
        print(" [*] Connecting to server ...")
        # RabbitMQサーバと接続
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="rabbitmq", port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
        # チャンネルの確立
        channel = connection.channel()
        # キューに接続
        channel.queue_declare(queue=self.queue_name(), durable=True)

        # コンシューマの登録
        def callback(channel, method, properties, body):
            print(f" [x] Received {body}")
            message = body.decode()
            self.filtered_dispatch(message)
            print(" [x] Done")
            # 受信したことをキューに知らせる
            channel.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_consume(queue=self.queue_name(), on_message_callback=callback)

        try:
            print(" [*] Waiting for messages. To exit press Ctrl+C")
            channel.start_consuming()
        except KeyboardInterrupt:
            print(" [x] Done")

    def queue_name(self) -> str:
        return "indexer.blog"

    def filtered_dispatch(self, text_message: str) -> NoReturn:
        """受信したメッセージを処理する"""
        print("メッセージを受信しました！")
        print("text_message = {}".format(text_message))
        # message = eval(text_message)
        # self.__save_blog_application_service.save(SaveBlogCommand())
