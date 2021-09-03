# Techosity Indexer

```bash
# コンテナの起動
$ docker-compose up --build

# Indexerを起動
$ docker-compose run --rm indexer python start_consuming.py
```

 - [RabbitMQのツール画面](http://localhost:15672/): ユーザー名とパスワードは、`guest`


```bash
curl -i -u guest:guest http://localhost:15672/api/vhosts

curl -XPOST http://localhost:15672//api/exchanges/blogs.save/publish -d '
{"properties":{},"routing_key":"my key","payload":"my body","payload_encoding":"string"}
'
```

## MQ

 - `pika`パッケージ
 - RabbitMQ

参考文献

 - [FastAPIでRabbitMQを使ってみる - Qiita](https://qiita.com/satto_sann/items/ca3647662843e65530c7)
 - [pythonでrabbimqを扱う - Qiita](https://qiita.com/mink0212/items/8d692e17b34793655c66)
 - [RabbitMQ tutorial - "Hello world!" 
 — RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
 - [python — Python and RabbitMQ-複数のチャネルからの消費イベントをリッスンする最良の方法？](https://www.it-mure.jp.net/ja/python/python-and-rabbitmq%E8%A4%87%E6%95%B0%E3%81%AE%E3%83%81%E3%83%A3%E3%83%8D%E3%83%AB%E3%81%8B%E3%82%89%E3%81%AE%E6%B6%88%E8%B2%BB%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%82%92%E3%83%AA%E3%83%83%E3%82%B9%E3%83%B3%E3%81%99%E3%82%8B%E6%9C%80%E8%89%AF%E3%81%AE%E6%96%B9%E6%B3%95%EF%BC%9F/1051158256/)
 - [IDDD_Samples/ExchangeListener.java at 05d95572f2ad6b85357b216d7d617b27359a360d · VaughnVernon/IDDD_Samples](https://github.com/VaughnVernon/IDDD_Samples/blob/05d95572f2ad6b85357b216d7d617b27359a360d/iddd_common/src/main/java/com/saasovation/common/port/adapter/messaging/rabbitmq/ExchangeListener.java)
