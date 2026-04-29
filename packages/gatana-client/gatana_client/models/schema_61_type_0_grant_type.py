from enum import Enum


class Schema61Type0GrantType(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"
    DEVICE_CODE = "device_code"

    def __str__(self) -> str:
        return str(self.value)
