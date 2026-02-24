from enum import Enum

class GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200Method(str, Enum):
    APIKEY = "apikey"
    NONE = "none"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
