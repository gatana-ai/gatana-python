from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_profiles_profile_id_tools_response_200_tools import GetProfilesProfileIdToolsResponse200Tools





T = TypeVar("T", bound="GetProfilesProfileIdToolsResponse200")



@_attrs_define
class GetProfilesProfileIdToolsResponse200:
    """ 
        Attributes:
            tools (GetProfilesProfileIdToolsResponse200Tools):
     """

    tools: GetProfilesProfileIdToolsResponse200Tools





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_profiles_profile_id_tools_response_200_tools import GetProfilesProfileIdToolsResponse200Tools
        tools = self.tools.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tools": tools,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_profiles_profile_id_tools_response_200_tools import GetProfilesProfileIdToolsResponse200Tools
        d = dict(src_dict)
        tools = GetProfilesProfileIdToolsResponse200Tools.from_dict(d.pop("tools"))




        get_profiles_profile_id_tools_response_200 = cls(
            tools=tools,
        )

        return get_profiles_profile_id_tools_response_200

