from enum import Enum


class Schema181(str, Enum):
    HTTPSTREAMING = "httpstreaming"
    SSE = "sse"
    STDIO = "stdio"

    def __str__(self) -> str:
        return str(self.value)
