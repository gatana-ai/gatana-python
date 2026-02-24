from enum import Enum

class CreateServerRequestTransportType(str, Enum):
    HOSTED = "hosted"
    HTTPSTREAMING = "httpstreaming"
    SSE = "sse"
    STDIO = "stdio"

    def __str__(self) -> str:
        return str(self.value)
