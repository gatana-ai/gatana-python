from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Schema487Item")


@_attrs_define
class Schema487Item:
    """
    Attributes:
        id (str):
        email (str):
        name (str):
        assigned_at (str):
        is_locked_by_org_owner (bool):
    """

    id: str
    email: str
    name: str
    assigned_at: str
    is_locked_by_org_owner: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name = self.name

        assigned_at = self.assigned_at

        is_locked_by_org_owner = self.is_locked_by_org_owner

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "email": email,
                "name": name,
                "assignedAt": assigned_at,
                "isLockedByOrgOwner": is_locked_by_org_owner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        name = d.pop("name")

        assigned_at = d.pop("assignedAt")

        is_locked_by_org_owner = d.pop("isLockedByOrgOwner")

        schema_487_item = cls(
            id=id,
            email=email,
            name=name,
            assigned_at=assigned_at,
            is_locked_by_org_owner=is_locked_by_org_owner,
        )

        return schema_487_item
