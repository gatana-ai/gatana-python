from enum import Enum


class Schema58ItemAction(str, Enum):
    DENY = "deny"
    LOG = "log"
    MODIFY = "modify"

    def __str__(self) -> str:
        return str(self.value)
