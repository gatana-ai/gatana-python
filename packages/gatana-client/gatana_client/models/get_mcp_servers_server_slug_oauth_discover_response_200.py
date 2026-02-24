from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.server_o_auth_metadata import ServerOAuthMetadata





T = TypeVar("T", bound="GetMcpServersServerSlugOauthDiscoverResponse200")



@_attrs_define
class GetMcpServersServerSlugOauthDiscoverResponse200:
    """ 
        Attributes:
            oauth_metadata (None | ServerOAuthMetadata):
     """

    oauth_metadata: None | ServerOAuthMetadata





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_o_auth_metadata import ServerOAuthMetadata
        oauth_metadata: dict[str, Any] | None
        if isinstance(self.oauth_metadata, ServerOAuthMetadata):
            oauth_metadata = self.oauth_metadata.to_dict()
        else:
            oauth_metadata = self.oauth_metadata


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "oauthMetadata": oauth_metadata,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_o_auth_metadata import ServerOAuthMetadata
        d = dict(src_dict)
        def _parse_oauth_metadata(data: object) -> None | ServerOAuthMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                oauth_metadata_type_0 = ServerOAuthMetadata.from_dict(data)



                return oauth_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerOAuthMetadata, data)

        oauth_metadata = _parse_oauth_metadata(d.pop("oauthMetadata"))


        get_mcp_servers_server_slug_oauth_discover_response_200 = cls(
            oauth_metadata=oauth_metadata,
        )

        return get_mcp_servers_server_slug_oauth_discover_response_200

