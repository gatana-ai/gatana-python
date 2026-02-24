from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.tenant_dto import TenantDto





T = TypeVar("T", bound="GetTenantsTenantIdResponse200")



@_attrs_define
class GetTenantsTenantIdResponse200:
    """ 
        Attributes:
            tenant (TenantDto):
     """

    tenant: TenantDto





    def to_dict(self) -> dict[str, Any]:
        from ..models.tenant_dto import TenantDto
        tenant = self.tenant.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tenant": tenant,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_dto import TenantDto
        d = dict(src_dict)
        tenant = TenantDto.from_dict(d.pop("tenant"))




        get_tenants_tenant_id_response_200 = cls(
            tenant=tenant,
        )

        return get_tenants_tenant_id_response_200

