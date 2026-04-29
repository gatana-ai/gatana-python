from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.audit_log_response import AuditLogResponse
    from ..models.schema_150 import Schema150


T = TypeVar("T", bound="PaginatedAuditLogResponse")


@_attrs_define
class PaginatedAuditLogResponse:
    """
    Attributes:
        pagination (Schema150):
        data (list[AuditLogResponse]):
    """

    pagination: Schema150
    data: list[AuditLogResponse]

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        data = []
        for componentsschemas_schema151_item_data in self.data:
            componentsschemas_schema151_item = componentsschemas_schema151_item_data.to_dict()
            data.append(componentsschemas_schema151_item)

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
        from ..models.audit_log_response import AuditLogResponse
        from ..models.schema_150 import Schema150

        d = dict(src_dict)
        pagination = Schema150.from_dict(d.pop("pagination"))

        data = []
        _data = d.pop("data")
        for componentsschemas_schema151_item_data in _data:
            componentsschemas_schema151_item = AuditLogResponse.from_dict(componentsschemas_schema151_item_data)

            data.append(componentsschemas_schema151_item)

        paginated_audit_log_response = cls(
            pagination=pagination,
            data=data,
        )

        return paginated_audit_log_response
