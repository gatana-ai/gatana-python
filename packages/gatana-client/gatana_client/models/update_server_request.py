from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.hosted_transport_config import HostedTransportConfig
  from ..models.http_streaming_transport_config import HttpStreamingTransportConfig
  from ..models.server_authorization import ServerAuthorization
  from ..models.sse_transport_config import SseTransportConfig
  from ..models.stdio_transport_config import StdioTransportConfig
  from ..models.update_server_request_oauth_client_configuration_type_0 import UpdateServerRequestOauthClientConfigurationType0
  from ..models.update_server_request_oauth_metadata_type_0 import UpdateServerRequestOauthMetadataType0
  from ..models.update_server_request_transport_config_type_4 import UpdateServerRequestTransportConfigType4





T = TypeVar("T", bound="UpdateServerRequest")



@_attrs_define
class UpdateServerRequest:
    """ 
        Attributes:
            slug (str | Unset):
            description (str | Unset):
            logo_url (str | Unset):
            url (str | Unset): The URL of the remote MCP server
            authorization (ServerAuthorization | Unset):
            transport_config (HostedTransportConfig | HttpStreamingTransportConfig | SseTransportConfig |
                StdioTransportConfig | Unset | UpdateServerRequestTransportConfigType4):
            oauth_metadata (None | Unset | UpdateServerRequestOauthMetadataType0):
            oauth_client_configuration (None | Unset | UpdateServerRequestOauthClientConfigurationType0):
     """

    slug: str | Unset = UNSET
    description: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    url: str | Unset = UNSET
    authorization: ServerAuthorization | Unset = UNSET
    transport_config: HostedTransportConfig | HttpStreamingTransportConfig | SseTransportConfig | StdioTransportConfig | Unset | UpdateServerRequestTransportConfigType4 = UNSET
    oauth_metadata: None | Unset | UpdateServerRequestOauthMetadataType0 = UNSET
    oauth_client_configuration: None | Unset | UpdateServerRequestOauthClientConfigurationType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.hosted_transport_config import HostedTransportConfig
        from ..models.stdio_transport_config import StdioTransportConfig
        from ..models.update_server_request_oauth_client_configuration_type_0 import UpdateServerRequestOauthClientConfigurationType0
        from ..models.server_authorization import ServerAuthorization
        from ..models.update_server_request_transport_config_type_4 import UpdateServerRequestTransportConfigType4
        from ..models.http_streaming_transport_config import HttpStreamingTransportConfig
        from ..models.sse_transport_config import SseTransportConfig
        from ..models.update_server_request_oauth_metadata_type_0 import UpdateServerRequestOauthMetadataType0
        slug = self.slug

        description = self.description

        logo_url = self.logo_url

        url = self.url

        authorization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorization, Unset):
            authorization = self.authorization.to_dict()

        transport_config: dict[str, Any] | Unset
        if isinstance(self.transport_config, Unset):
            transport_config = UNSET
        elif isinstance(self.transport_config, HttpStreamingTransportConfig):
            transport_config = self.transport_config.to_dict()
        elif isinstance(self.transport_config, HostedTransportConfig):
            transport_config = self.transport_config.to_dict()
        elif isinstance(self.transport_config, StdioTransportConfig):
            transport_config = self.transport_config.to_dict()
        elif isinstance(self.transport_config, SseTransportConfig):
            transport_config = self.transport_config.to_dict()
        else:
            transport_config = self.transport_config.to_dict()


        oauth_metadata: dict[str, Any] | None | Unset
        if isinstance(self.oauth_metadata, Unset):
            oauth_metadata = UNSET
        elif isinstance(self.oauth_metadata, UpdateServerRequestOauthMetadataType0):
            oauth_metadata = self.oauth_metadata.to_dict()
        else:
            oauth_metadata = self.oauth_metadata

        oauth_client_configuration: dict[str, Any] | None | Unset
        if isinstance(self.oauth_client_configuration, Unset):
            oauth_client_configuration = UNSET
        elif isinstance(self.oauth_client_configuration, UpdateServerRequestOauthClientConfigurationType0):
            oauth_client_configuration = self.oauth_client_configuration.to_dict()
        else:
            oauth_client_configuration = self.oauth_client_configuration


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if url is not UNSET:
            field_dict["url"] = url
        if authorization is not UNSET:
            field_dict["authorization"] = authorization
        if transport_config is not UNSET:
            field_dict["transportConfig"] = transport_config
        if oauth_metadata is not UNSET:
            field_dict["oauthMetadata"] = oauth_metadata
        if oauth_client_configuration is not UNSET:
            field_dict["oauthClientConfiguration"] = oauth_client_configuration

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hosted_transport_config import HostedTransportConfig
        from ..models.http_streaming_transport_config import HttpStreamingTransportConfig
        from ..models.server_authorization import ServerAuthorization
        from ..models.sse_transport_config import SseTransportConfig
        from ..models.stdio_transport_config import StdioTransportConfig
        from ..models.update_server_request_oauth_client_configuration_type_0 import UpdateServerRequestOauthClientConfigurationType0
        from ..models.update_server_request_oauth_metadata_type_0 import UpdateServerRequestOauthMetadataType0
        from ..models.update_server_request_transport_config_type_4 import UpdateServerRequestTransportConfigType4
        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        description = d.pop("description", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        url = d.pop("url", UNSET)

        _authorization = d.pop("authorization", UNSET)
        authorization: ServerAuthorization | Unset
        if isinstance(_authorization,  Unset):
            authorization = UNSET
        else:
            authorization = ServerAuthorization.from_dict(_authorization)




        def _parse_transport_config(data: object) -> HostedTransportConfig | HttpStreamingTransportConfig | SseTransportConfig | StdioTransportConfig | Unset | UpdateServerRequestTransportConfigType4:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transport_config_type_0 = HttpStreamingTransportConfig.from_dict(data)



                return transport_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transport_config_type_1 = HostedTransportConfig.from_dict(data)



                return transport_config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transport_config_type_2 = StdioTransportConfig.from_dict(data)



                return transport_config_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transport_config_type_3 = SseTransportConfig.from_dict(data)



                return transport_config_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            transport_config_type_4 = UpdateServerRequestTransportConfigType4.from_dict(data)



            return transport_config_type_4

        transport_config = _parse_transport_config(d.pop("transportConfig", UNSET))


        def _parse_oauth_metadata(data: object) -> None | Unset | UpdateServerRequestOauthMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                oauth_metadata_type_0 = UpdateServerRequestOauthMetadataType0.from_dict(data)



                return oauth_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateServerRequestOauthMetadataType0, data)

        oauth_metadata = _parse_oauth_metadata(d.pop("oauthMetadata", UNSET))


        def _parse_oauth_client_configuration(data: object) -> None | Unset | UpdateServerRequestOauthClientConfigurationType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                oauth_client_configuration_type_0 = UpdateServerRequestOauthClientConfigurationType0.from_dict(data)



                return oauth_client_configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateServerRequestOauthClientConfigurationType0, data)

        oauth_client_configuration = _parse_oauth_client_configuration(d.pop("oauthClientConfiguration", UNSET))


        update_server_request = cls(
            slug=slug,
            description=description,
            logo_url=logo_url,
            url=url,
            authorization=authorization,
            transport_config=transport_config,
            oauth_metadata=oauth_metadata,
            oauth_client_configuration=oauth_client_configuration,
        )


        update_server_request.additional_properties = d
        return update_server_request

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
