from enum import Enum


class Schema188(str, Enum):
    NODE24 = "node24"

    def __str__(self) -> str:
        return str(self.value)
