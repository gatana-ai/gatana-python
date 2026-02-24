from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.post_mcp_servers_server_slug_tools_tool_name_call_body_args import PostMcpServersServerSlugToolsToolNameCallBodyArgs





T = TypeVar("T", bound="PostMcpServersServerSlugToolsToolNameCallBody")



@_attrs_define
class PostMcpServersServerSlugToolsToolNameCallBody:
    """ 
        Attributes:
            args (PostMcpServersServerSlugToolsToolNameCallBodyArgs):
     """

    args: PostMcpServersServerSlugToolsToolNameCallBodyArgs
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_mcp_servers_server_slug_tools_tool_name_call_body_args import PostMcpServersServerSlugToolsToolNameCallBodyArgs
        args = self.args.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "args": args,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_mcp_servers_server_slug_tools_tool_name_call_body_args import PostMcpServersServerSlugToolsToolNameCallBodyArgs
        d = dict(src_dict)
        args = PostMcpServersServerSlugToolsToolNameCallBodyArgs.from_dict(d.pop("args"))




        post_mcp_servers_server_slug_tools_tool_name_call_body = cls(
            args=args,
        )


        post_mcp_servers_server_slug_tools_tool_name_call_body.additional_properties = d
        return post_mcp_servers_server_slug_tools_tool_name_call_body

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
