from dataclasses import dataclass


@dataclass(init=False, frozen=True, unsafe_hash=True)
class Query:
    parameter: str

    def __init__(self, parameter: str):
        assert parameter is not None, "引数parameterは必須です。"
        assert isinstance(parameter, str), "引数parameterに{}が指定されています。文字列を指定して下さい。".format(type(parameter))
        super().__setattr__("parameter", parameter)
