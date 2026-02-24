from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_sandbox_id_audit_logs_id_response_200_pagination import (
        GetSandboxIdAuditLogsIdResponse200Pagination,
    )
    from ..models.sandbox_audit_log import SandboxAuditLog


T = TypeVar("T", bound="GetSandboxIdAuditLogsIdResponse200")


@_attrs_define
class GetSandboxIdAuditLogsIdResponse200:
    """
    Attributes:
        pagination (GetSandboxIdAuditLogsIdResponse200Pagination):
        data (list[SandboxAuditLog]):
    """

    pagination: GetSandboxIdAuditLogsIdResponse200Pagination
    data: list[SandboxAuditLog]

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "pagination": pagination,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sandbox_id_audit_logs_id_response_200_pagination import (
            GetSandboxIdAuditLogsIdResponse200Pagination,
        )
        from ..models.sandbox_audit_log import SandboxAuditLog

        d = dict(src_dict)
        pagination = GetSandboxIdAuditLogsIdResponse200Pagination.from_dict(d.pop("pagination"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = SandboxAuditLog.from_dict(data_item_data)

            data.append(data_item)

        get_sandbox_id_audit_logs_id_response_200 = cls(
            pagination=pagination,
            data=data,
        )

        return get_sandbox_id_audit_logs_id_response_200
