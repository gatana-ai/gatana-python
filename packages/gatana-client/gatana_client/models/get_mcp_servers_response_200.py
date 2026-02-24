from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_mcp_servers_response_200_servers_item import GetMcpServersResponse200ServersItem





T = TypeVar("T", bound="GetMcpServersResponse200")



@_attrs_define
class GetMcpServersResponse200:
    """ 
        Attributes:
            servers (list[GetMcpServersResponse200ServersItem]):
     """

    servers: list[GetMcpServersResponse200ServersItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_mcp_servers_response_200_servers_item import GetMcpServersResponse200ServersItem
        servers = []
        for servers_item_data in self.servers:
            servers_item = servers_item_data.to_dict()
            servers.append(servers_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "servers": servers,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_mcp_servers_response_200_servers_item import GetMcpServersResponse200ServersItem
        d = dict(src_dict)
        servers = []
        _servers = d.pop("servers")
        for servers_item_data in (_servers):
            servers_item = GetMcpServersResponse200ServersItem.from_dict(servers_item_data)



            servers.append(servers_item)


        get_mcp_servers_response_200 = cls(
            servers=servers,
        )

        return get_mcp_servers_response_200

