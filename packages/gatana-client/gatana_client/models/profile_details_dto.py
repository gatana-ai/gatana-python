from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_447_item import Schema447Item


T = TypeVar("T", bound="ProfileDetailsDto")


@_attrs_define
class ProfileDetailsDto:
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
        servers (list[Schema447Item]):
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
    servers: list[Schema447Item]

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

        servers = []
        for componentsschemas_schema447_item_data in self.servers:
            componentsschemas_schema447_item = componentsschemas_schema447_item_data.to_dict()
            servers.append(componentsschemas_schema447_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenantId": tenant_id,
                "id": id,
                "createdBy": created_by,
                "name": name,
                "description": description,
                "isOpenToAllUsers": is_open_to_all_users,
                "isRestrictive": is_restrictive,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "servers": servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_447_item import Schema447Item

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

        servers = []
        _servers = d.pop("servers")
        for componentsschemas_schema447_item_data in _servers:
            componentsschemas_schema447_item = Schema447Item.from_dict(componentsschemas_schema447_item_data)

            servers.append(componentsschemas_schema447_item)

        profile_details_dto = cls(
            tenant_id=tenant_id,
            id=id,
            created_by=created_by,
            name=name,
            description=description,
            is_open_to_all_users=is_open_to_all_users,
            is_restrictive=is_restrictive,
            created_at=created_at,
            updated_at=updated_at,
            servers=servers,
        )

        return profile_details_dto
