from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_243_item import Schema243Item
    from ..models.schema_245_item import Schema245Item


T = TypeVar("T", bound="GetMembersResponse")


@_attrs_define
class GetMembersResponse:
    """
    Attributes:
        teams (list[Schema243Item]):
        users (list[Schema245Item]):
    """

    teams: list[Schema243Item]
    users: list[Schema245Item]

    def to_dict(self) -> dict[str, Any]:
        teams = []
        for componentsschemas_schema243_item_data in self.teams:
            componentsschemas_schema243_item = componentsschemas_schema243_item_data.to_dict()
            teams.append(componentsschemas_schema243_item)

        users = []
        for componentsschemas_schema245_item_data in self.users:
            componentsschemas_schema245_item = componentsschemas_schema245_item_data.to_dict()
            users.append(componentsschemas_schema245_item)

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
        from ..models.schema_243_item import Schema243Item
        from ..models.schema_245_item import Schema245Item

        d = dict(src_dict)
        teams = []
        _teams = d.pop("teams")
        for componentsschemas_schema243_item_data in _teams:
            componentsschemas_schema243_item = Schema243Item.from_dict(componentsschemas_schema243_item_data)

            teams.append(componentsschemas_schema243_item)

        users = []
        _users = d.pop("users")
        for componentsschemas_schema245_item_data in _users:
            componentsschemas_schema245_item = Schema245Item.from_dict(componentsschemas_schema245_item_data)

            users.append(componentsschemas_schema245_item)

        get_members_response = cls(
            teams=teams,
            users=users,
        )

        return get_members_response
