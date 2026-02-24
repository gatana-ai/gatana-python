from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.server_credentials_dto import ServerCredentialsDto





T = TypeVar("T", bound="GetMcpServersServerSlugCredentialsProfileResponse200")



@_attrs_define
class GetMcpServersServerSlugCredentialsProfileResponse200:
    """ 
        Attributes:
            credentials (None | ServerCredentialsDto):
     """

    credentials: None | ServerCredentialsDto





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_credentials_dto import ServerCredentialsDto
        credentials: dict[str, Any] | None
        if isinstance(self.credentials, ServerCredentialsDto):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "credentials": credentials,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_credentials_dto import ServerCredentialsDto
        d = dict(src_dict)
        def _parse_credentials(data: object) -> None | ServerCredentialsDto:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = ServerCredentialsDto.from_dict(data)



                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerCredentialsDto, data)

        credentials = _parse_credentials(d.pop("credentials"))


        get_mcp_servers_server_slug_credentials_profile_response_200 = cls(
            credentials=credentials,
        )

        return get_mcp_servers_server_slug_credentials_profile_response_200

