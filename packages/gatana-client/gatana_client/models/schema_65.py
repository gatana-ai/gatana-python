from enum import Enum

class Schema65(str, Enum):
    ADMIN = "admin"
    MAINTAINER = "maintainer"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
