from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.profile_details_dto import ProfileDetailsDto





T = TypeVar("T", bound="GetProfilesProfileIdResponse200")



@_attrs_define
class GetProfilesProfileIdResponse200:
    """ 
        Attributes:
            profile (ProfileDetailsDto):
     """

    profile: ProfileDetailsDto





    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_details_dto import ProfileDetailsDto
        profile = self.profile.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "profile": profile,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_details_dto import ProfileDetailsDto
        d = dict(src_dict)
        profile = ProfileDetailsDto.from_dict(d.pop("profile"))




        get_profiles_profile_id_response_200 = cls(
            profile=profile,
        )

        return get_profiles_profile_id_response_200

