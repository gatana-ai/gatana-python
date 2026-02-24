from enum import Enum


class Schema40(str, Enum):
    MEMBER = "member"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
