from abc import ABC, abstractmethod, abstractproperty
from typing import TypedDict, List


# Must present params
class SerializeErrorParamsBase(TypedDict):
    message: str


# Optional params
class SerializeErrorParams(SerializeErrorParamsBase, total=False):
    field: str


class CustomError(ABC):

    @abstractproperty
    def status_code(self) -> int:
        pass

    @abstractmethod
    def serialize_errors(self) -> List[SerializeErrorParams]:
        pass


if __name__ == "__main__":
    a = CustomError()
