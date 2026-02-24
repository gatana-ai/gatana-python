from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.profile import Profile





T = TypeVar("T", bound="GetProfilesResponse200")



@_attrs_define
class GetProfilesResponse200:
    """ 
        Attributes:
            profiles (list[Profile]):
     """

    profiles: list[Profile]





    def to_dict(self) -> dict[str, Any]:
        from ..models.profile import Profile
        profiles = []
        for profiles_item_data in self.profiles:
            profiles_item = profiles_item_data.to_dict()
            profiles.append(profiles_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "profiles": profiles,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile import Profile
        d = dict(src_dict)
        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in (_profiles):
            profiles_item = Profile.from_dict(profiles_item_data)



            profiles.append(profiles_item)


        get_profiles_response_200 = cls(
            profiles=profiles,
        )

        return get_profiles_response_200

