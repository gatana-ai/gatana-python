from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutProfilesProfileIdBody")



@_attrs_define
class PutProfilesProfileIdBody:
    """ 
        Attributes:
            name (str | Unset):
            description (str | Unset):
            is_open_to_all_users (bool | Unset):
            is_restrictive (bool | Unset):
            server_ids (list[str] | Unset):
     """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    is_open_to_all_users: bool | Unset = UNSET
    is_restrictive: bool | Unset = UNSET
    server_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        is_open_to_all_users = self.is_open_to_all_users

        is_restrictive = self.is_restrictive

        server_ids: list[str] | Unset = UNSET
        if not isinstance(self.server_ids, Unset):
            server_ids = self.server_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_open_to_all_users is not UNSET:
            field_dict["isOpenToAllUsers"] = is_open_to_all_users
        if is_restrictive is not UNSET:
            field_dict["isRestrictive"] = is_restrictive
        if server_ids is not UNSET:
            field_dict["serverIds"] = server_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        is_open_to_all_users = d.pop("isOpenToAllUsers", UNSET)

        is_restrictive = d.pop("isRestrictive", UNSET)

        server_ids = cast(list[str], d.pop("serverIds", UNSET))


        put_profiles_profile_id_body = cls(
            name=name,
            description=description,
            is_open_to_all_users=is_open_to_all_users,
            is_restrictive=is_restrictive,
            server_ids=server_ids,
        )


        put_profiles_profile_id_body.additional_properties = d
        return put_profiles_profile_id_body

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
