from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sandbox_audit_log import SandboxAuditLog
    from ..models.schema_41 import Schema41


T = TypeVar("T", bound="PaginatedSandboxAuditLog")


@_attrs_define
class PaginatedSandboxAuditLog:
    """
    Attributes:
        pagination (Schema41):
        data (list[SandboxAuditLog]):
    """

    pagination: Schema41
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
        from ..models.sandbox_audit_log import SandboxAuditLog
        from ..models.schema_41 import Schema41

        d = dict(src_dict)
        pagination = Schema41.from_dict(d.pop("pagination"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = SandboxAuditLog.from_dict(data_item_data)

            data.append(data_item)

        paginated_sandbox_audit_log = cls(
            pagination=pagination,
            data=data,
        )

        return paginated_sandbox_audit_log
