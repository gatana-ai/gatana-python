from enum import Enum


class Schema1087(str, Enum):
    GATANA = "gatana"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
