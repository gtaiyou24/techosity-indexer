from enum import Enum


class Protocol(Enum):
    HTTP = 'http'
    HTTPS = 'https'

    @staticmethod
    def value_of(protocol: str):
        if (protocol == Protocol.HTTPS.name) or (protocol == Protocol.HTTPS.value):
            return Protocol.HTTPS
        elif (protocol == Protocol.HTTP.name) or (protocol == Protocol.HTTP.value):
            return Protocol.HTTP
        else:
            raise Exception("該当のProtocolが存在しません。 (protocol = {})".format(protocol))
