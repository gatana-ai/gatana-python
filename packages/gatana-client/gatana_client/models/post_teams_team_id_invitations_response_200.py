from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.team_invitation import TeamInvitation





T = TypeVar("T", bound="PostTeamsTeamIdInvitationsResponse200")



@_attrs_define
class PostTeamsTeamIdInvitationsResponse200:
    """ 
        Attributes:
            invitation (TeamInvitation):
     """

    invitation: TeamInvitation





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_invitation import TeamInvitation
        invitation = self.invitation.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "invitation": invitation,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_invitation import TeamInvitation
        d = dict(src_dict)
        invitation = TeamInvitation.from_dict(d.pop("invitation"))




        post_teams_team_id_invitations_response_200 = cls(
            invitation=invitation,
        )

        return post_teams_team_id_invitations_response_200

