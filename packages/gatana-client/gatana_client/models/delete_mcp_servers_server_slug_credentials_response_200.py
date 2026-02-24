from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DeleteMcpServersServerSlugCredentialsResponse200")



@_attrs_define
class DeleteMcpServersServerSlugCredentialsResponse200:
    """ 
        Attributes:
            success (bool):
            deleted_count (float):
     """

    success: bool
    deleted_count: float





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        deleted_count = self.deleted_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "success": success,
            "deletedCount": deleted_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        deleted_count = d.pop("deletedCount")

        delete_mcp_servers_server_slug_credentials_response_200 = cls(
            success=success,
            deleted_count=deleted_count,
        )

        return delete_mcp_servers_server_slug_credentials_response_200

