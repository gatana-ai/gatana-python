from enum import Enum

class StdioTransportConfigOutputTransport(str, Enum):
    HTTPSTREAMING = "httpstreaming"
    SSE = "sse"
    STDIO = "stdio"

    def __str__(self) -> str:
        return str(self.value)
