from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_teams_team_id_members_response_200_members_item import GetTeamsTeamIdMembersResponse200MembersItem





T = TypeVar("T", bound="GetTeamsTeamIdMembersResponse200")



@_attrs_define
class GetTeamsTeamIdMembersResponse200:
    """ 
        Attributes:
            members (list[GetTeamsTeamIdMembersResponse200MembersItem]):
     """

    members: list[GetTeamsTeamIdMembersResponse200MembersItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_teams_team_id_members_response_200_members_item import GetTeamsTeamIdMembersResponse200MembersItem
        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "members": members,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_teams_team_id_members_response_200_members_item import GetTeamsTeamIdMembersResponse200MembersItem
        d = dict(src_dict)
        members = []
        _members = d.pop("members")
        for members_item_data in (_members):
            members_item = GetTeamsTeamIdMembersResponse200MembersItem.from_dict(members_item_data)



            members.append(members_item)


        get_teams_team_id_members_response_200 = cls(
            members=members,
        )

        return get_teams_team_id_members_response_200

