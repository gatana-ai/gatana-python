from enum import Enum

class HostedTransportConfigOutputRuntime(str, Enum):
    NODE24 = "node24"

    def __str__(self) -> str:
        return str(self.value)
