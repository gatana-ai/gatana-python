from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetMcpServersResponse200ServersItemUsage")



@_attrs_define
class GetMcpServersResponse200ServersItemUsage:
    """ 
        Attributes:
            last_seven_days (float):
     """

    last_seven_days: float





    def to_dict(self) -> dict[str, Any]:
        last_seven_days = self.last_seven_days


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "lastSevenDays": last_seven_days,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_seven_days = d.pop("lastSevenDays")

        get_mcp_servers_response_200_servers_item_usage = cls(
            last_seven_days=last_seven_days,
        )

        return get_mcp_servers_response_200_servers_item_usage

