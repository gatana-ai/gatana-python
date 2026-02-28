from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetDeploymentsLogsResponse200Logs")


@_attrs_define
class GetDeploymentsLogsResponse200Logs:
    """
    Attributes:
        stdout (str):
        stderr (str):
    """

    stdout: str
    stderr: str

    def to_dict(self) -> dict[str, Any]:
        stdout = self.stdout

        stderr = self.stderr

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "stdout": stdout,
                "stderr": stderr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stdout = d.pop("stdout")

        stderr = d.pop("stderr")

        get_deployments_logs_response_200_logs = cls(
            stdout=stdout,
            stderr=stderr,
        )

        return get_deployments_logs_response_200_logs
