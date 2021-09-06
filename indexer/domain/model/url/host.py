from dataclasses import dataclass


@dataclass(init=False, frozen=True, unsafe_hash=True)
class Host:
    name: str

    def __init__(self, name: str):
        assert name is not None and name != '', "引数nameは必須です。"
        assert isinstance(name, str), "引数nameに{}が指定されています。文字列を指定して下さい。".format(type(name))
        super().__setattr__("name", name)
