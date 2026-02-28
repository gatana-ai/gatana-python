from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hosted_transport_config_output import HostedTransportConfigOutput
    from ..models.http_streaming_transport_config_output import HttpStreamingTransportConfigOutput
    from ..models.schema_58_type_3 import Schema58Type3
    from ..models.server_authorization_output import ServerAuthorizationOutput
    from ..models.server_o_auth_client_configuration import ServerOAuthClientConfiguration
    from ..models.server_o_auth_metadata import ServerOAuthMetadata
    from ..models.sse_transport_config_output import SseTransportConfigOutput
    from ..models.stdio_transport_config_output import StdioTransportConfigOutput


T = TypeVar("T", bound="ServerDto")


@_attrs_define
class ServerDto:
    """
    Attributes:
        id (float):
        slug (str):
        tenant_id (str):
        name (str): DEPRECATED. Field will be removed in future versions. Please use slug instead.
        description (str):
        authorization (ServerAuthorizationOutput):
        transport_config (HostedTransportConfigOutput | HttpStreamingTransportConfigOutput | Schema58Type3 |
            SseTransportConfigOutput | StdioTransportConfigOutput):
        oauth_client_configuration (None | ServerOAuthClientConfiguration):
        oauth_metadata (None | ServerOAuthMetadata):
        is_enabled (bool):
        last_tool_refresh_at (None | str):
        timeout_protocol (int):
        timeout_total (int):
        reset_timeout_on_progress_notification (bool):
        created_at (str):
        updated_at (str):
        logo_url (str | Unset):
    """

    id: float
    slug: str
    tenant_id: str
    name: str
    description: str
    authorization: ServerAuthorizationOutput
    transport_config: (
        HostedTransportConfigOutput
        | HttpStreamingTransportConfigOutput
        | Schema58Type3
        | SseTransportConfigOutput
        | StdioTransportConfigOutput
    )
    oauth_client_configuration: None | ServerOAuthClientConfiguration
    oauth_metadata: None | ServerOAuthMetadata
    is_enabled: bool
    last_tool_refresh_at: None | str
    timeout_protocol: int
    timeout_total: int
    reset_timeout_on_progress_notification: bool
    created_at: str
    updated_at: str
    logo_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.http_streaming_transport_config_output import HttpStreamingTransportConfigOutput
        from ..models.schema_58_type_3 import Schema58Type3
        from ..models.server_o_auth_client_configuration import ServerOAuthClientConfiguration
        from ..models.server_o_auth_metadata import ServerOAuthMetadata
        from ..models.sse_transport_config_output import SseTransportConfigOutput
        from ..models.stdio_transport_config_output import StdioTransportConfigOutput

        id = self.id

        slug = self.slug

        tenant_id = self.tenant_id

        name = self.name

        description = self.description

        authorization = self.authorization.to_dict()

        transport_config: dict[str, Any]
        if isinstance(self.transport_config, HttpStreamingTransportConfigOutput):
            transport_config = self.transport_config.to_dict()
        elif isinstance(self.transport_config, StdioTransportConfigOutput):
            transport_config = self.transport_config.to_dict()
        elif isinstance(self.transport_config, SseTransportConfigOutput):
            transport_config = self.transport_config.to_dict()
        elif isinstance(self.transport_config, Schema58Type3):
            transport_config = self.transport_config.to_dict()
        else:
            transport_config = self.transport_config.to_dict()

        oauth_client_configuration: dict[str, Any] | None
        if isinstance(self.oauth_client_configuration, ServerOAuthClientConfiguration):
            oauth_client_configuration = self.oauth_client_configuration.to_dict()
        else:
            oauth_client_configuration = self.oauth_client_configuration

        oauth_metadata: dict[str, Any] | None
        if isinstance(self.oauth_metadata, ServerOAuthMetadata):
            oauth_metadata = self.oauth_metadata.to_dict()
        else:
            oauth_metadata = self.oauth_metadata

        is_enabled = self.is_enabled

        last_tool_refresh_at: None | str
        last_tool_refresh_at = self.last_tool_refresh_at

        timeout_protocol = self.timeout_protocol

        timeout_total = self.timeout_total

        reset_timeout_on_progress_notification = self.reset_timeout_on_progress_notification

        created_at = self.created_at

        updated_at = self.updated_at

        logo_url = self.logo_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "tenantId": tenant_id,
                "name": name,
                "description": description,
                "authorization": authorization,
                "transportConfig": transport_config,
                "oauthClientConfiguration": oauth_client_configuration,
                "oauthMetadata": oauth_metadata,
                "isEnabled": is_enabled,
                "lastToolRefreshAt": last_tool_refresh_at,
                "timeoutProtocol": timeout_protocol,
                "timeoutTotal": timeout_total,
                "resetTimeoutOnProgressNotification": reset_timeout_on_progress_notification,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hosted_transport_config_output import HostedTransportConfigOutput
        from ..models.http_streaming_transport_config_output import HttpStreamingTransportConfigOutput
        from ..models.schema_58_type_3 import Schema58Type3
        from ..models.server_authorization_output import ServerAuthorizationOutput
        from ..models.server_o_auth_client_configuration import ServerOAuthClientConfiguration
        from ..models.server_o_auth_metadata import ServerOAuthMetadata
        from ..models.sse_transport_config_output import SseTransportConfigOutput
        from ..models.stdio_transport_config_output import StdioTransportConfigOutput

        d = dict(src_dict)
        id = d.pop("id")

        slug = d.pop("slug")

        tenant_id = d.pop("tenantId")

        name = d.pop("name")

        description = d.pop("description")

        authorization = ServerAuthorizationOutput.from_dict(d.pop("authorization"))

        def _parse_transport_config(
            data: object,
        ) -> (
            HostedTransportConfigOutput
            | HttpStreamingTransportConfigOutput
            | Schema58Type3
            | SseTransportConfigOutput
            | StdioTransportConfigOutput
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema58_type_0 = HttpStreamingTransportConfigOutput.from_dict(data)

                return componentsschemas_schema58_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema58_type_1 = StdioTransportConfigOutput.from_dict(data)

                return componentsschemas_schema58_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema58_type_2 = SseTransportConfigOutput.from_dict(data)

                return componentsschemas_schema58_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema58_type_3 = Schema58Type3.from_dict(data)

                return componentsschemas_schema58_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_schema58_type_4 = HostedTransportConfigOutput.from_dict(data)

            return componentsschemas_schema58_type_4

        transport_config = _parse_transport_config(d.pop("transportConfig"))

        def _parse_oauth_client_configuration(data: object) -> None | ServerOAuthClientConfiguration:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema59_type_1 = ServerOAuthClientConfiguration.from_dict(data)

                return componentsschemas_schema59_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerOAuthClientConfiguration, data)

        oauth_client_configuration = _parse_oauth_client_configuration(d.pop("oauthClientConfiguration"))

        def _parse_oauth_metadata(data: object) -> None | ServerOAuthMetadata:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema60_type_1 = ServerOAuthMetadata.from_dict(data)

                return componentsschemas_schema60_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerOAuthMetadata, data)

        oauth_metadata = _parse_oauth_metadata(d.pop("oauthMetadata"))

        is_enabled = d.pop("isEnabled")

        def _parse_last_tool_refresh_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_tool_refresh_at = _parse_last_tool_refresh_at(d.pop("lastToolRefreshAt"))

        timeout_protocol = d.pop("timeoutProtocol")

        timeout_total = d.pop("timeoutTotal")

        reset_timeout_on_progress_notification = d.pop("resetTimeoutOnProgressNotification")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        logo_url = d.pop("logoUrl", UNSET)

        server_dto = cls(
            id=id,
            slug=slug,
            tenant_id=tenant_id,
            name=name,
            description=description,
            authorization=authorization,
            transport_config=transport_config,
            oauth_client_configuration=oauth_client_configuration,
            oauth_metadata=oauth_metadata,
            is_enabled=is_enabled,
            last_tool_refresh_at=last_tool_refresh_at,
            timeout_protocol=timeout_protocol,
            timeout_total=timeout_total,
            reset_timeout_on_progress_notification=reset_timeout_on_progress_notification,
            created_at=created_at,
            updated_at=updated_at,
            logo_url=logo_url,
        )

        return server_dto
