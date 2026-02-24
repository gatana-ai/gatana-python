from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.team_member import TeamMember
  from ..models.user import User





T = TypeVar("T", bound="GetTeamsTeamIdMembersResponse200MembersItem")



@_attrs_define
class GetTeamsTeamIdMembersResponse200MembersItem:
    """ 
        Attributes:
            member (TeamMember):
            user (User):
     """

    member: TeamMember
    user: User





    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User
        from ..models.team_member import TeamMember
        member = self.member.to_dict()

        user = self.user.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "member": member,
            "user": user,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_member import TeamMember
        from ..models.user import User
        d = dict(src_dict)
        member = TeamMember.from_dict(d.pop("member"))




        user = User.from_dict(d.pop("user"))




        get_teams_team_id_members_response_200_members_item = cls(
            member=member,
            user=user,
        )

        return get_teams_team_id_members_response_200_members_item

