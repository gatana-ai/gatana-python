from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.audit_log_response import AuditLogResponse
  from ..models.paginated_audit_logs_pagination import PaginatedAuditLogsPagination





T = TypeVar("T", bound="PaginatedAuditLogs")



@_attrs_define
class PaginatedAuditLogs:
    """ 
        Attributes:
            data (list[AuditLogResponse]):
            pagination (PaginatedAuditLogsPagination):
     """

    data: list[AuditLogResponse]
    pagination: PaginatedAuditLogsPagination





    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_log_response import AuditLogResponse
        from ..models.paginated_audit_logs_pagination import PaginatedAuditLogsPagination
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        pagination = self.pagination.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "pagination": pagination,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_log_response import AuditLogResponse
        from ..models.paginated_audit_logs_pagination import PaginatedAuditLogsPagination
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = AuditLogResponse.from_dict(data_item_data)



            data.append(data_item)


        pagination = PaginatedAuditLogsPagination.from_dict(d.pop("pagination"))




        paginated_audit_logs = cls(
            data=data,
            pagination=pagination,
        )

        return paginated_audit_logs

