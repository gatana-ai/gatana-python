from enum import Enum


class Schema28(str, Enum):
    APIKEY = "apikey"
    NONE = "none"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
