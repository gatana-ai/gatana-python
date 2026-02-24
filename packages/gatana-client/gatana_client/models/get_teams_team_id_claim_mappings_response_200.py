from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.team_claim_mapping import TeamClaimMapping





T = TypeVar("T", bound="GetTeamsTeamIdClaimMappingsResponse200")



@_attrs_define
class GetTeamsTeamIdClaimMappingsResponse200:
    """ 
        Attributes:
            claim_mappings (list[TeamClaimMapping]):
     """

    claim_mappings: list[TeamClaimMapping]





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_claim_mapping import TeamClaimMapping
        claim_mappings = []
        for claim_mappings_item_data in self.claim_mappings:
            claim_mappings_item = claim_mappings_item_data.to_dict()
            claim_mappings.append(claim_mappings_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "claimMappings": claim_mappings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_claim_mapping import TeamClaimMapping
        d = dict(src_dict)
        claim_mappings = []
        _claim_mappings = d.pop("claimMappings")
        for claim_mappings_item_data in (_claim_mappings):
            claim_mappings_item = TeamClaimMapping.from_dict(claim_mappings_item_data)



            claim_mappings.append(claim_mappings_item)


        get_teams_team_id_claim_mappings_response_200 = cls(
            claim_mappings=claim_mappings,
        )

        return get_teams_team_id_claim_mappings_response_200

