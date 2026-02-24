from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_server_request_transport_type import CreateServerRequestTransportType






T = TypeVar("T", bound="CreateServerRequest")



@_attrs_define
class CreateServerRequest:
    """ 
        Attributes:
            transport_type (CreateServerRequestTransportType): Transport type: httpstreaming, sse, stdio, or hosted
            slug (str): Technical identifier.
     """

    transport_type: CreateServerRequestTransportType
    slug: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        transport_type = self.transport_type.value

        slug = self.slug


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "transportType": transport_type,
            "slug": slug,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transport_type = CreateServerRequestTransportType(d.pop("transportType"))




        slug = d.pop("slug")

        create_server_request = cls(
            transport_type=transport_type,
            slug=slug,
        )


        create_server_request.additional_properties = d
        return create_server_request

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
