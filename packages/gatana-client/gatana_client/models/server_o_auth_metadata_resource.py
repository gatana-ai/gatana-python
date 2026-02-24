from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ServerOAuthMetadataResource")



@_attrs_define
class ServerOAuthMetadataResource:
    """ 
        Attributes:
            id (str):  Default: ''.
            available_scopes (list[str]):
            metadata_url (str):  Default: ''.
     """

    available_scopes: list[str]
    id: str = ''
    metadata_url: str = ''





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        available_scopes = self.available_scopes



        metadata_url = self.metadata_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "availableScopes": available_scopes,
            "metadataUrl": metadata_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        available_scopes = cast(list[str], d.pop("availableScopes"))


        metadata_url = d.pop("metadataUrl")

        server_o_auth_metadata_resource = cls(
            id=id,
            available_scopes=available_scopes,
            metadata_url=metadata_url,
        )

        return server_o_auth_metadata_resource

