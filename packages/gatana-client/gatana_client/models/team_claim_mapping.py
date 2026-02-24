from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TeamClaimMapping")



@_attrs_define
class TeamClaimMapping:
    """ 
        Attributes:
            id (str):
            tenant_id (str):
            team_id (str):
            claim_key (str):
            claim_value (str):
            created_at (str):
     """

    id: str
    tenant_id: str
    team_id: str
    claim_key: str
    claim_value: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        team_id = self.team_id

        claim_key = self.claim_key

        claim_value = self.claim_value

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "tenantId": tenant_id,
            "teamId": team_id,
            "claimKey": claim_key,
            "claimValue": claim_value,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        tenant_id = d.pop("tenantId")

        team_id = d.pop("teamId")

        claim_key = d.pop("claimKey")

        claim_value = d.pop("claimValue")

        created_at = d.pop("createdAt")

        team_claim_mapping = cls(
            id=id,
            tenant_id=tenant_id,
            team_id=team_id,
            claim_key=claim_key,
            claim_value=claim_value,
            created_at=created_at,
        )

        return team_claim_mapping

