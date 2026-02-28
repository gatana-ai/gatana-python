from enum import Enum


class GetCredentialTokenResponseType(str, Enum):
    APIKEY = "apikey"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
