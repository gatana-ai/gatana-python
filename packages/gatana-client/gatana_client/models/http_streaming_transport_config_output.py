from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="HttpStreamingTransportConfigOutput")



@_attrs_define
class HttpStreamingTransportConfigOutput:
    """ 
        Attributes:
            type_ (Literal['httpstreaming']):
            url (str):
            headers (list[list[str]] | Unset):
     """

    type_: Literal['httpstreaming']
    url: str
    headers: list[list[str]] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url = self.url

        headers: list[list[str]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = []
                for headers_item_item_data in headers_item_data:
                    headers_item_item: str
                    headers_item_item = headers_item_item_data
                    headers_item.append(headers_item_item)


                headers.append(headers_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "url": url,
        })
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['httpstreaming'] , d.pop("type"))
        if type_ != 'httpstreaming':
            raise ValueError(f"type must match const 'httpstreaming', got '{type_}'")

        url = d.pop("url")

        _headers = d.pop("headers", UNSET)
        headers: list[list[str]] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = []
                _headers_item = headers_item_data
                for headers_item_item_data in (_headers_item):
                    def _parse_headers_item_item(data: object) -> str:
                        return cast(str, data)

                    headers_item_item = _parse_headers_item_item(headers_item_item_data)

                    headers_item.append(headers_item_item)

                headers.append(headers_item)


        http_streaming_transport_config_output = cls(
            type_=type_,
            url=url,
            headers=headers,
        )

        return http_streaming_transport_config_output

