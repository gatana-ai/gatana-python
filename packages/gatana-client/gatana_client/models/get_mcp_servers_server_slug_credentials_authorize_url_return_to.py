from enum import Enum

class GetMcpServersServerSlugCredentialsAuthorizeUrlReturnTo(str, Enum):
    DETAILS = "details"
    PROFILE = "profile"
    SETTINGS = "settings"
    THANK_YOU_PAGE = "thank-you-page"

    def __str__(self) -> str:
        return str(self.value)
