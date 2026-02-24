from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="Profile")



@_attrs_define
class Profile:
    """ 
        Attributes:
            tenant_id (str):
            id (str):
            created_by (float):
            name (str):
            description (str):
            is_open_to_all_users (bool):
            is_restrictive (bool):
            created_at (str):
            updated_at (str):
     """

    tenant_id: str
    id: str
    created_by: float
    name: str
    description: str
    is_open_to_all_users: bool
    is_restrictive: bool
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        id = self.id

        created_by = self.created_by

        name = self.name

        description = self.description

        is_open_to_all_users = self.is_open_to_all_users

        is_restrictive = self.is_restrictive

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tenantId": tenant_id,
            "id": id,
            "createdBy": created_by,
            "name": name,
            "description": description,
            "isOpenToAllUsers": is_open_to_all_users,
            "isRestrictive": is_restrictive,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_id = d.pop("tenantId")

        id = d.pop("id")

        created_by = d.pop("createdBy")

        name = d.pop("name")

        description = d.pop("description")

        is_open_to_all_users = d.pop("isOpenToAllUsers")

        is_restrictive = d.pop("isRestrictive")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        profile = cls(
            tenant_id=tenant_id,
            id=id,
            created_by=created_by,
            name=name,
            description=description,
            is_open_to_all_users=is_open_to_all_users,
            is_restrictive=is_restrictive,
            created_at=created_at,
            updated_at=updated_at,
        )

        return profile

