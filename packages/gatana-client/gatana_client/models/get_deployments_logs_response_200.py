from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_deployments_logs_response_200_logs import GetDeploymentsLogsResponse200Logs


T = TypeVar("T", bound="GetDeploymentsLogsResponse200")


@_attrs_define
class GetDeploymentsLogsResponse200:
    """
    Attributes:
        logs (GetDeploymentsLogsResponse200Logs):
    """

    logs: GetDeploymentsLogsResponse200Logs

    def to_dict(self) -> dict[str, Any]:
        logs = self.logs.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "logs": logs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_deployments_logs_response_200_logs import GetDeploymentsLogsResponse200Logs

        d = dict(src_dict)
        logs = GetDeploymentsLogsResponse200Logs.from_dict(d.pop("logs"))

        get_deployments_logs_response_200 = cls(
            logs=logs,
        )

        return get_deployments_logs_response_200
