from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.schema_65 import Schema65






T = TypeVar("T", bound="ServerMemberType1")



@_attrs_define
class ServerMemberType1:
    """ 
        Attributes:
            tenant_id (str):
            server_id (float):
            role (Schema65):
            created_at (str):
            updated_at (str):
            user_id (None):
            team_id (str):
     """

    tenant_id: str
    server_id: float
    role: Schema65
    created_at: str
    updated_at: str
    user_id: None
    team_id: str





    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        server_id = self.server_id

        role = self.role.value

        created_at = self.created_at

        updated_at = self.updated_at

        user_id = self.user_id

        team_id = self.team_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tenantId": tenant_id,
            "serverId": server_id,
            "role": role,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "userId": user_id,
            "teamId": team_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_id = d.pop("tenantId")

        server_id = d.pop("serverId")

        role = Schema65(d.pop("role"))




        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        user_id = d.pop("userId")

        team_id = d.pop("teamId")

        server_member_type_1 = cls(
            tenant_id=tenant_id,
            server_id=server_id,
            role=role,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            team_id=team_id,
        )

        return server_member_type_1

