from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TeamWithMemberCount")



@_attrs_define
class TeamWithMemberCount:
    """ 
        Attributes:
            id (str):
            tenant_id (str):
            name (str):
            description (str):
            created_at (str):
            updated_at (str):
            member_count (float):
     """

    id: str
    tenant_id: str
    name: str
    description: str
    created_at: str
    updated_at: str
    member_count: float





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        name = self.name

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at

        member_count = self.member_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "tenantId": tenant_id,
            "name": name,
            "description": description,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "memberCount": member_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        tenant_id = d.pop("tenantId")

        name = d.pop("name")

        description = d.pop("description")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        member_count = d.pop("memberCount")

        team_with_member_count = cls(
            id=id,
            tenant_id=tenant_id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            member_count=member_count,
        )

        return team_with_member_count

