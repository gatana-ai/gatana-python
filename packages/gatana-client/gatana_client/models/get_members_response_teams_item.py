from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schema_66 import Schema66

T = TypeVar("T", bound="GetMembersResponseTeamsItem")


@_attrs_define
class GetMembersResponseTeamsItem:
    """
    Attributes:
        role (Schema66):
        id (str):
        name (str):
    """

    role: Schema66
    id: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = Schema66(d.pop("role"))

        id = d.pop("id")

        name = d.pop("name")

        get_members_response_teams_item = cls(
            role=role,
            id=id,
            name=name,
        )

        return get_members_response_teams_item
