from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.server_tool_dto import ServerToolDto





T = TypeVar("T", bound="GetMcpServersServerSlugToolsResponse200")



@_attrs_define
class GetMcpServersServerSlugToolsResponse200:
    """ 
        Attributes:
            tools (list[ServerToolDto]):
     """

    tools: list[ServerToolDto]





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_tool_dto import ServerToolDto
        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tools": tools,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_tool_dto import ServerToolDto
        d = dict(src_dict)
        tools = []
        _tools = d.pop("tools")
        for tools_item_data in (_tools):
            tools_item = ServerToolDto.from_dict(tools_item_data)



            tools.append(tools_item)


        get_mcp_servers_server_slug_tools_response_200 = cls(
            tools=tools,
        )

        return get_mcp_servers_server_slug_tools_response_200

