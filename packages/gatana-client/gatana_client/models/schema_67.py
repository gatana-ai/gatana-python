from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.team_with_member_count import TeamWithMemberCount





T = TypeVar("T", bound="Schema67")



@_attrs_define
class Schema67:
    """ 
        Attributes:
            team (TeamWithMemberCount):
     """

    team: TeamWithMemberCount





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_with_member_count import TeamWithMemberCount
        team = self.team.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "team": team,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_with_member_count import TeamWithMemberCount
        d = dict(src_dict)
        team = TeamWithMemberCount.from_dict(d.pop("team"))




        schema_67 = cls(
            team=team,
        )

        return schema_67

