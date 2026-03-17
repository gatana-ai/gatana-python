from enum import Enum


class Schema111(str, Enum):
    PLAYGROUND_CONVERSION = "playground-conversion"
    SIGNUP = "signup"

    def __str__(self) -> str:
        return str(self.value)
