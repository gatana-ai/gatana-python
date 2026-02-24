from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.team_claim_mapping import TeamClaimMapping





T = TypeVar("T", bound="PostTeamsTeamIdClaimMappingsResponse200")



@_attrs_define
class PostTeamsTeamIdClaimMappingsResponse200:
    """ 
        Attributes:
            claim_mapping (TeamClaimMapping):
     """

    claim_mapping: TeamClaimMapping





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_claim_mapping import TeamClaimMapping
        claim_mapping = self.claim_mapping.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "claimMapping": claim_mapping,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_claim_mapping import TeamClaimMapping
        d = dict(src_dict)
        claim_mapping = TeamClaimMapping.from_dict(d.pop("claimMapping"))




        post_teams_team_id_claim_mappings_response_200 = cls(
            claim_mapping=claim_mapping,
        )

        return post_teams_team_id_claim_mappings_response_200

