from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_mcp_servers_server_slug_tools_tool_name_call_response_200_result import (
        PostMcpServersServerSlugToolsToolNameCallResponse200Result,
    )


T = TypeVar("T", bound="PostMcpServersServerSlugToolsToolNameCallResponse200")


@_attrs_define
class PostMcpServersServerSlugToolsToolNameCallResponse200:
    """
    Attributes:
        result (PostMcpServersServerSlugToolsToolNameCallResponse200Result | Unset):
    """

    result: PostMcpServersServerSlugToolsToolNameCallResponse200Result | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_mcp_servers_server_slug_tools_tool_name_call_response_200_result import (
            PostMcpServersServerSlugToolsToolNameCallResponse200Result,
        )

        d = dict(src_dict)
        _result = d.pop("result", UNSET)
        result: PostMcpServersServerSlugToolsToolNameCallResponse200Result | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = PostMcpServersServerSlugToolsToolNameCallResponse200Result.from_dict(_result)

        post_mcp_servers_server_slug_tools_tool_name_call_response_200 = cls(
            result=result,
        )

        return post_mcp_servers_server_slug_tools_tool_name_call_response_200
