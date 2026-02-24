from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.server_credentials_dto import ServerCredentialsDto





T = TypeVar("T", bound="GetMcpServersServerSlugCredentialsResponse200")



@_attrs_define
class GetMcpServersServerSlugCredentialsResponse200:
    """ 
        Attributes:
            credentials (list[ServerCredentialsDto]):
     """

    credentials: list[ServerCredentialsDto]





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_credentials_dto import ServerCredentialsDto
        credentials = []
        for credentials_item_data in self.credentials:
            credentials_item = credentials_item_data.to_dict()
            credentials.append(credentials_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "credentials": credentials,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_credentials_dto import ServerCredentialsDto
        d = dict(src_dict)
        credentials = []
        _credentials = d.pop("credentials")
        for credentials_item_data in (_credentials):
            credentials_item = ServerCredentialsDto.from_dict(credentials_item_data)



            credentials.append(credentials_item)


        get_mcp_servers_server_slug_credentials_response_200 = cls(
            credentials=credentials,
        )

        return get_mcp_servers_server_slug_credentials_response_200

