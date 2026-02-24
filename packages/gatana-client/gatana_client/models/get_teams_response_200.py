from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.team_with_member_count import TeamWithMemberCount





T = TypeVar("T", bound="GetTeamsResponse200")



@_attrs_define
class GetTeamsResponse200:
    """ 
        Attributes:
            teams (list[TeamWithMemberCount]):
     """

    teams: list[TeamWithMemberCount]





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_with_member_count import TeamWithMemberCount
        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "teams": teams,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_with_member_count import TeamWithMemberCount
        d = dict(src_dict)
        teams = []
        _teams = d.pop("teams")
        for teams_item_data in (_teams):
            teams_item = TeamWithMemberCount.from_dict(teams_item_data)



            teams.append(teams_item)


        get_teams_response_200 = cls(
            teams=teams,
        )

        return get_teams_response_200

