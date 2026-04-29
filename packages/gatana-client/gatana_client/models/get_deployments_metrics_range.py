from enum import Enum


class GetDeploymentsMetricsRange(str, Enum):
    VALUE_0 = "1h"
    VALUE_1 = "6h"
    VALUE_2 = "24h"

    def __str__(self) -> str:
        return str(self.value)
