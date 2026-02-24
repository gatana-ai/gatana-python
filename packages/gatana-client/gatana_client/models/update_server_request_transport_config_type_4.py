from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="UpdateServerRequestTransportConfigType4")



@_attrs_define
class UpdateServerRequestTransportConfigType4:
    """ 
        Attributes:
            type_ (Literal['self']):
            id (str):
     """

    type_: Literal['self']
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['self'] , d.pop("type"))
        if type_ != 'self':
            raise ValueError(f"type must match const 'self', got '{type_}'")

        id = d.pop("id")

        update_server_request_transport_config_type_4 = cls(
            type_=type_,
            id=id,
        )


        update_server_request_transport_config_type_4.additional_properties = d
        return update_server_request_transport_config_type_4

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
