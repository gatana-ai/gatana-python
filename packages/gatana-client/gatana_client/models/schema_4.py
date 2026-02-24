from enum import Enum

class Schema4(str, Enum):
    APIKEY = "apikey"
    NONE = "none"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
