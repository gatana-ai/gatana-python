from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PutMcpServersServerSlugIsEnabledResponse200")



@_attrs_define
class PutMcpServersServerSlugIsEnabledResponse200:
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

        put_mcp_servers_server_slug_is_enabled_response_200 = cls(
            success=success,
        )

        return put_mcp_servers_server_slug_is_enabled_response_200

