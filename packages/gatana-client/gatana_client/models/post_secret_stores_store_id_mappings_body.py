from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostSecretStoresStoreIdMappingsBody")



@_attrs_define
class PostSecretStoresStoreIdMappingsBody:
    """ 
        Attributes:
            name (str):
            secret_identifier (str):
     """

    name: str
    secret_identifier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        secret_identifier = self.secret_identifier


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "secretIdentifier": secret_identifier,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        secret_identifier = d.pop("secretIdentifier")

        post_secret_stores_store_id_mappings_body = cls(
            name=name,
            secret_identifier=secret_identifier,
        )


        post_secret_stores_store_id_mappings_body.additional_properties = d
        return post_secret_stores_store_id_mappings_body

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
