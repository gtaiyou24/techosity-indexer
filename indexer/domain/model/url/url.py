from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import urlparse, ParseResult

from domain.model.url import Protocol, Host, Path, Query


@dataclass(init=False, frozen=True, unsafe_hash=True)
class URL:
    protocol: Protocol
    host: Host
    path: Path
    query: Query

    def __init__(self, protocol: Protocol, host: Host, path: Path, query: Query):
        assert protocol is not None, "引数protocolにNoneが指定されています。引数protocolは必須です。"
        assert host is not None, "引数hostにNoneが指定されています。引数hostは必須です。"
        assert path is not None, "引数pathにNoneが指定されています。引数pathは必須です。"
        assert query is not None, "引数queryにNoneが指定されています。引数queryは必須です。"
        assert isinstance(protocol, Protocol), \
            "引数protocolに{}が指定されています。引数protocolには文字列を指定して下さい。".format(type(protocol))
        assert isinstance(host, Host), \
            "引数hostに{}が指定されています。引数hostには文字列を指定して下さい。".format(type(host))
        assert isinstance(path, Path), \
            "引数pathに{}が指定されています。引数pathには文字列を指定して下さい。".format(type(path))
        assert isinstance(query, Query), \
            "引数queryに{}が指定されています。引数queryには文字列を指定して下さい。".format(type(query))
        super().__setattr__("protocol", protocol)
        super().__setattr__("host", host)
        super().__setattr__("path", path)
        super().__setattr__("query", query)

    @staticmethod
    def of(absolute_url: str) -> URL:
        assert URL._is_absolute_url(absolute_url), "{}は完全URLではありません。完全URLを指定して下さい。".format(absolute_url)

        parse_result: ParseResult = urlparse(absolute_url)
        return URL(
            Protocol.value_of(parse_result.scheme),
            Host(parse_result.netloc),
            Path(parse_result.path),
            Query(parse_result.query)
        )

    @staticmethod
    def _is_absolute_url(url: str) -> bool:
        return re.match(r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", url) is not None

    def absolute_url(self) -> str:
        return self.protocol.name + "://" + self.host.name + "" + self.path.name + "?" + self.query.parameter
