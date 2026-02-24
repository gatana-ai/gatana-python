from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.team_invitation import TeamInvitation





T = TypeVar("T", bound="GetTeamsTeamIdInvitationsResponse200")



@_attrs_define
class GetTeamsTeamIdInvitationsResponse200:
    """ 
        Attributes:
            invitations (list[TeamInvitation]):
     """

    invitations: list[TeamInvitation]





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_invitation import TeamInvitation
        invitations = []
        for invitations_item_data in self.invitations:
            invitations_item = invitations_item_data.to_dict()
            invitations.append(invitations_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "invitations": invitations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_invitation import TeamInvitation
        d = dict(src_dict)
        invitations = []
        _invitations = d.pop("invitations")
        for invitations_item_data in (_invitations):
            invitations_item = TeamInvitation.from_dict(invitations_item_data)



            invitations.append(invitations_item)


        get_teams_team_id_invitations_response_200 = cls(
            invitations=invitations,
        )

        return get_teams_team_id_invitations_response_200

