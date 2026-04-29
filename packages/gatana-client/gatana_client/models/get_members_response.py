from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_263_item import Schema263Item
    from ..models.schema_264_item import Schema264Item


T = TypeVar("T", bound="GetMembersResponse")


@_attrs_define
class GetMembersResponse:
    """
    Attributes:
        teams (list[Schema263Item]):
        users (list[Schema264Item]):
    """

    teams: list[Schema263Item]
    users: list[Schema264Item]

    def to_dict(self) -> dict[str, Any]:
        teams = []
        for componentsschemas_schema263_item_data in self.teams:
            componentsschemas_schema263_item = componentsschemas_schema263_item_data.to_dict()
            teams.append(componentsschemas_schema263_item)

        users = []
        for componentsschemas_schema264_item_data in self.users:
            componentsschemas_schema264_item = componentsschemas_schema264_item_data.to_dict()
            users.append(componentsschemas_schema264_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "teams": teams,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_263_item import Schema263Item
        from ..models.schema_264_item import Schema264Item

        d = dict(src_dict)
        teams = []
        _teams = d.pop("teams")
        for componentsschemas_schema263_item_data in _teams:
            componentsschemas_schema263_item = Schema263Item.from_dict(componentsschemas_schema263_item_data)

            teams.append(componentsschemas_schema263_item)

        users = []
        _users = d.pop("users")
        for componentsschemas_schema264_item_data in _users:
            componentsschemas_schema264_item = Schema264Item.from_dict(componentsschemas_schema264_item_data)

            users.append(componentsschemas_schema264_item)

        get_members_response = cls(
            teams=teams,
            users=users,
        )

        return get_members_response
