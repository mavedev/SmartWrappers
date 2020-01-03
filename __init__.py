from typing import Any
import constants


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

    def steal(self, other: 'SmartWrapper') -> None:
        self.__value, other.__value = other.__value, None


SoftSmartWrapper = SmartWrapper


class StrictSmartWrapper(SmartWrapper):
    def __init__(self, value: Any, type_: type) -> None:
        super().__init__(value)
        self.__type_ = type_

    def __new__(cls, *args, **kwargs):
        StrictSmartWrapper.__check(*args, **kwargs)
        return super(StrictSmartWrapper, cls).__new__(cls)

    def __call__(self, value: Any = None) -> Any:
        if value:
            self.__check(value, self.__type_)
        return super().__call__(value)

    def steal(self, other: 'StrictSmartWrapper') -> None:
        if self():
            self.__check(other(), self.__type_)
        super().steal(other)

    @staticmethod
    def __check(value: Any, type_: type) -> None:
        if not isinstance(value, type_):
            raise AssertionError(constants.WRONG_TYPE)


def wrap(value: Any) -> SmartWrapper:
    return SmartWrapper(value)


def wrap_strictly(value: Any, type_: type) -> StrictSmartWrapper:
    return StrictSmartWrapper(value, type_)
