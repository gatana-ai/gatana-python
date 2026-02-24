from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_mcp_servers_server_slug_credentials_authorize_url_response_200_method import GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200Method
from ..types import UNSET, Unset






T = TypeVar("T", bound="GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200")



@_attrs_define
class GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200:
    """ 
        Attributes:
            method (GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200Method):
            url (str | Unset):
     """

    method: GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200Method
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "method": method,
        })
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = GetMcpServersServerSlugCredentialsAuthorizeUrlResponse200Method(d.pop("method"))




        url = d.pop("url", UNSET)

        get_mcp_servers_server_slug_credentials_authorize_url_response_200 = cls(
            method=method,
            url=url,
        )

        return get_mcp_servers_server_slug_credentials_authorize_url_response_200

