from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DeleteProfilesProfileIdResponse200")



@_attrs_define
class DeleteProfilesProfileIdResponse200:
    """ 
        Attributes:
            success (bool):
     """

    success: bool





    def to_dict(self) -> dict[str, Any]:
        success = self.success


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "success": success,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        delete_profiles_profile_id_response_200 = cls(
            success=success,
        )

        return delete_profiles_profile_id_response_200

