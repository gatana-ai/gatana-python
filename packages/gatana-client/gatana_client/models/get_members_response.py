from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_members_response_teams_item import GetMembersResponseTeamsItem
  from ..models.get_members_response_users_item import GetMembersResponseUsersItem





T = TypeVar("T", bound="GetMembersResponse")



@_attrs_define
class GetMembersResponse:
    """ 
        Attributes:
            teams (list[GetMembersResponseTeamsItem]):
            users (list[GetMembersResponseUsersItem]):
     """

    teams: list[GetMembersResponseTeamsItem]
    users: list[GetMembersResponseUsersItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_members_response_users_item import GetMembersResponseUsersItem
        from ..models.get_members_response_teams_item import GetMembersResponseTeamsItem
        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)



        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "teams": teams,
            "users": users,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_members_response_teams_item import GetMembersResponseTeamsItem
        from ..models.get_members_response_users_item import GetMembersResponseUsersItem
        d = dict(src_dict)
        teams = []
        _teams = d.pop("teams")
        for teams_item_data in (_teams):
            teams_item = GetMembersResponseTeamsItem.from_dict(teams_item_data)



            teams.append(teams_item)


        users = []
        _users = d.pop("users")
        for users_item_data in (_users):
            users_item = GetMembersResponseUsersItem.from_dict(users_item_data)



            users.append(users_item)


        get_members_response = cls(
            teams=teams,
            users=users,
        )

        return get_members_response

