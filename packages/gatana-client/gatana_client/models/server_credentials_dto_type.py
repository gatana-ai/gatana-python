from enum import Enum

class ServerCredentialsDtoType(str, Enum):
    APIKEY = "apikey"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
