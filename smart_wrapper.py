from typing import Any


class SmartWrapper:
    def __init__(self, value: Any) -> None:
        self.__value = value

    def __call__(self, value: Any = None) -> Any:
        if value:
            self.__value = value
        else:
            return self.__value

    def __str__(self) -> str:
        return str(self.__value)

    def __repr__(self) -> str:
        return repr(self.__value)

    def gettype(self) -> type:
        return type(self.__value)

    def hasattr(self, attr: str) -> bool:
        return hasattr(self.__value, attr)


def wrap(value: Any) -> SmartWrapper:
    return SmartWrapper(value)
