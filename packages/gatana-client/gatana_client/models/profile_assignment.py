from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileAssignment")


@_attrs_define
class ProfileAssignment:
    """
    Attributes:
        profile_id (str):
        is_locked_by_org_owner (bool):
    """

    profile_id: str
    is_locked_by_org_owner: bool

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        is_locked_by_org_owner = self.is_locked_by_org_owner

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "profileId": profile_id,
                "isLockedByOrgOwner": is_locked_by_org_owner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        profile_id = d.pop("profileId")

        is_locked_by_org_owner = d.pop("isLockedByOrgOwner")

        profile_assignment = cls(
            profile_id=profile_id,
            is_locked_by_org_owner=is_locked_by_org_owner,
        )

        return profile_assignment
