from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="PutMcpServersServerSlugConfigBodyType3")



@_attrs_define
class PutMcpServersServerSlugConfigBodyType3:
    """ 
        Attributes:
            type_ (Literal['sse'] | Unset):
            url (str | Unset):
            headers (list[list[str]] | Unset):
     """

    type_: Literal['sse'] | Unset = UNSET
    url: str | Unset = UNSET
    headers: list[list[str]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url = self.url

        headers: list[list[str]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for componentsschemas_schema22_item_data in self.headers:
                componentsschemas_schema22_item = []
                for componentsschemas_schema22_item_item_data in componentsschemas_schema22_item_data:
                    componentsschemas_schema22_item_item: str
                    componentsschemas_schema22_item_item = componentsschemas_schema22_item_item_data
                    componentsschemas_schema22_item.append(componentsschemas_schema22_item_item)


                headers.append(componentsschemas_schema22_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['sse'] | Unset , d.pop("type", UNSET))
        if type_ != 'sse'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'sse', got '{type_}'")

        url = d.pop("url", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: list[list[str]] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for componentsschemas_schema22_item_data in _headers:
                componentsschemas_schema22_item = []
                _componentsschemas_schema22_item = componentsschemas_schema22_item_data
                for componentsschemas_schema22_item_item_data in (_componentsschemas_schema22_item):
                    def _parse_componentsschemas_schema22_item_item(data: object) -> str:
                        return cast(str, data)

                    componentsschemas_schema22_item_item = _parse_componentsschemas_schema22_item_item(componentsschemas_schema22_item_item_data)

                    componentsschemas_schema22_item.append(componentsschemas_schema22_item_item)

                headers.append(componentsschemas_schema22_item)


        put_mcp_servers_server_slug_config_body_type_3 = cls(
            type_=type_,
            url=url,
            headers=headers,
        )


        put_mcp_servers_server_slug_config_body_type_3.additional_properties = d
        return put_mcp_servers_server_slug_config_body_type_3

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
