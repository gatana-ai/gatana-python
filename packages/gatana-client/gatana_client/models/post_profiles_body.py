from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostProfilesBody")



@_attrs_define
class PostProfilesBody:
    """ 
        Attributes:
            name (str):
            description (str):
            is_open_to_all_users (bool):
            is_restrictive (bool):
     """

    name: str
    description: str
    is_open_to_all_users: bool
    is_restrictive: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        is_open_to_all_users = self.is_open_to_all_users

        is_restrictive = self.is_restrictive


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "description": description,
            "isOpenToAllUsers": is_open_to_all_users,
            "isRestrictive": is_restrictive,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        is_open_to_all_users = d.pop("isOpenToAllUsers")

        is_restrictive = d.pop("isRestrictive")

        post_profiles_body = cls(
            name=name,
            description=description,
            is_open_to_all_users=is_open_to_all_users,
            is_restrictive=is_restrictive,
        )


        post_profiles_body.additional_properties = d
        return post_profiles_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
