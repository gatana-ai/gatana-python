from enum import Enum


class Schema375(str, Enum):
    FAILED = "Failed"
    PENDING = "Pending"
    READY = "Ready"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
