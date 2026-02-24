from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.schema_39 import Schema39
from ..types import UNSET, Unset






T = TypeVar("T", bound="AuthMetadataUser")



@_attrs_define
class AuthMetadataUser:
    """ 
        Attributes:
            id (float):
            sub (str):
            tenant_id (str):
            name (str):
            api_key (str):
            email (str):
            role (Schema39):
            is_service_account (bool):
            created_at (str):
            updated_at (str):
            is_super_administrator (bool | Unset):
     """

    id: float
    sub: str
    tenant_id: str
    name: str
    api_key: str
    email: str
    role: Schema39
    is_service_account: bool
    created_at: str
    updated_at: str
    is_super_administrator: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sub = self.sub

        tenant_id = self.tenant_id

        name = self.name

        api_key = self.api_key

        email = self.email

        role = self.role.value

        is_service_account = self.is_service_account

        created_at = self.created_at

        updated_at = self.updated_at

        is_super_administrator = self.is_super_administrator


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "sub": sub,
            "tenantId": tenant_id,
            "name": name,
            "apiKey": api_key,
            "email": email,
            "role": role,
            "isServiceAccount": is_service_account,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })
        if is_super_administrator is not UNSET:
            field_dict["isSuperAdministrator"] = is_super_administrator

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sub = d.pop("sub")

        tenant_id = d.pop("tenantId")

        name = d.pop("name")

        api_key = d.pop("apiKey")

        email = d.pop("email")

        role = Schema39(d.pop("role"))




        is_service_account = d.pop("isServiceAccount")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        is_super_administrator = d.pop("isSuperAdministrator", UNSET)

        auth_metadata_user = cls(
            id=id,
            sub=sub,
            tenant_id=tenant_id,
            name=name,
            api_key=api_key,
            email=email,
            role=role,
            is_service_account=is_service_account,
            created_at=created_at,
            updated_at=updated_at,
            is_super_administrator=is_super_administrator,
        )

        return auth_metadata_user

