from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schema_59 import Schema59
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hosted_transport_config import HostedTransportConfig
    from ..models.http_streaming_transport_config import HttpStreamingTransportConfig
    from ..models.schema_27 import Schema27
    from ..models.schema_31_type_4 import Schema31Type4
    from ..models.schema_50_type_0 import Schema50Type0
    from ..models.schema_51_type_0 import Schema51Type0
    from ..models.schema_58_item import Schema58Item
    from ..models.sse_transport_config import SseTransportConfig
    from ..models.stdio_transport_config import StdioTransportConfig


T = TypeVar("T", bound="UpdateServerRequest")


@_attrs_define
class UpdateServerRequest:
    """
    Attributes:
        slug (str | Unset):
        description (str | Unset):
        logo_url (str | Unset):
        url (str | Unset):
        authorization (Schema27 | Unset):
        transport_config (HostedTransportConfig | HttpStreamingTransportConfig | Schema31Type4 | SseTransportConfig |
            StdioTransportConfig | Unset):
        oauth_metadata (None | Schema50Type0 | Unset):
        oauth_client_configuration (None | Schema51Type0 | Unset):
        timeout_protocol (int | Unset):
        timeout_total (int | Unset):
        reset_timeout_on_progress_notification (bool | Unset):
        is_output_compression_enabled (bool | Unset):
        is_output_compression_transform_enabled (bool | Unset):
        output_compression_threshold_bytes (int | Unset):
        firewall_rules (list[Schema58Item] | Unset):
        visibility (Schema59 | Unset):
    """

    slug: str | Unset = UNSET
    description: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    url: str | Unset = UNSET
    authorization: Schema27 | Unset = UNSET
    transport_config: (
        HostedTransportConfig
        | HttpStreamingTransportConfig
        | Schema31Type4
        | SseTransportConfig
        | StdioTransportConfig
        | Unset
    ) = UNSET
    oauth_metadata: None | Schema50Type0 | Unset = UNSET
    oauth_client_configuration: None | Schema51Type0 | Unset = UNSET
    timeout_protocol: int | Unset = UNSET
    timeout_total: int | Unset = UNSET
    reset_timeout_on_progress_notification: bool | Unset = UNSET
    is_output_compression_enabled: bool | Unset = UNSET
    is_output_compression_transform_enabled: bool | Unset = UNSET
    output_compression_threshold_bytes: int | Unset = UNSET
    firewall_rules: list[Schema58Item] | Unset = UNSET
    visibility: Schema59 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hosted_transport_config import HostedTransportConfig
        from ..models.http_streaming_transport_config import HttpStreamingTransportConfig
        from ..models.schema_50_type_0 import Schema50Type0
        from ..models.schema_51_type_0 import Schema51Type0
        from ..models.sse_transport_config import SseTransportConfig
        from ..models.stdio_transport_config import StdioTransportConfig

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
        elif isinstance(self.oauth_metadata, Schema50Type0):
            oauth_metadata = self.oauth_metadata.to_dict()
        else:
            oauth_metadata = self.oauth_metadata

        oauth_client_configuration: dict[str, Any] | None | Unset
        if isinstance(self.oauth_client_configuration, Unset):
            oauth_client_configuration = UNSET
        elif isinstance(self.oauth_client_configuration, Schema51Type0):
            oauth_client_configuration = self.oauth_client_configuration.to_dict()
        else:
            oauth_client_configuration = self.oauth_client_configuration

        timeout_protocol = self.timeout_protocol

        timeout_total = self.timeout_total

        reset_timeout_on_progress_notification = self.reset_timeout_on_progress_notification

        is_output_compression_enabled = self.is_output_compression_enabled

        is_output_compression_transform_enabled = self.is_output_compression_transform_enabled

        output_compression_threshold_bytes = self.output_compression_threshold_bytes

        firewall_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.firewall_rules, Unset):
            firewall_rules = []
            for componentsschemas_schema58_item_data in self.firewall_rules:
                componentsschemas_schema58_item = componentsschemas_schema58_item_data.to_dict()
                firewall_rules.append(componentsschemas_schema58_item)

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if timeout_protocol is not UNSET:
            field_dict["timeoutProtocol"] = timeout_protocol
        if timeout_total is not UNSET:
            field_dict["timeoutTotal"] = timeout_total
        if reset_timeout_on_progress_notification is not UNSET:
            field_dict["resetTimeoutOnProgressNotification"] = reset_timeout_on_progress_notification
        if is_output_compression_enabled is not UNSET:
            field_dict["isOutputCompressionEnabled"] = is_output_compression_enabled
        if is_output_compression_transform_enabled is not UNSET:
            field_dict["isOutputCompressionTransformEnabled"] = is_output_compression_transform_enabled
        if output_compression_threshold_bytes is not UNSET:
            field_dict["outputCompressionThresholdBytes"] = output_compression_threshold_bytes
        if firewall_rules is not UNSET:
            field_dict["firewallRules"] = firewall_rules
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hosted_transport_config import HostedTransportConfig
        from ..models.http_streaming_transport_config import HttpStreamingTransportConfig
        from ..models.schema_27 import Schema27
        from ..models.schema_31_type_4 import Schema31Type4
        from ..models.schema_50_type_0 import Schema50Type0
        from ..models.schema_51_type_0 import Schema51Type0
        from ..models.schema_58_item import Schema58Item
        from ..models.sse_transport_config import SseTransportConfig
        from ..models.stdio_transport_config import StdioTransportConfig

        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        description = d.pop("description", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        url = d.pop("url", UNSET)

        _authorization = d.pop("authorization", UNSET)
        authorization: Schema27 | Unset
        if isinstance(_authorization, Unset):
            authorization = UNSET
        else:
            authorization = Schema27.from_dict(_authorization)

        def _parse_transport_config(
            data: object,
        ) -> (
            HostedTransportConfig
            | HttpStreamingTransportConfig
            | Schema31Type4
            | SseTransportConfig
            | StdioTransportConfig
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema31_type_0 = HttpStreamingTransportConfig.from_dict(data)

                return componentsschemas_schema31_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema31_type_1 = HostedTransportConfig.from_dict(data)

                return componentsschemas_schema31_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema31_type_2 = StdioTransportConfig.from_dict(data)

                return componentsschemas_schema31_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema31_type_3 = SseTransportConfig.from_dict(data)

                return componentsschemas_schema31_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_schema31_type_4 = Schema31Type4.from_dict(data)

            return componentsschemas_schema31_type_4

        transport_config = _parse_transport_config(d.pop("transportConfig", UNSET))

        def _parse_oauth_metadata(data: object) -> None | Schema50Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema50_type_0 = Schema50Type0.from_dict(data)

                return componentsschemas_schema50_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Schema50Type0 | Unset, data)

        oauth_metadata = _parse_oauth_metadata(d.pop("oauthMetadata", UNSET))

        def _parse_oauth_client_configuration(data: object) -> None | Schema51Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema51_type_0 = Schema51Type0.from_dict(data)

                return componentsschemas_schema51_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Schema51Type0 | Unset, data)

        oauth_client_configuration = _parse_oauth_client_configuration(d.pop("oauthClientConfiguration", UNSET))

        timeout_protocol = d.pop("timeoutProtocol", UNSET)

        timeout_total = d.pop("timeoutTotal", UNSET)

        reset_timeout_on_progress_notification = d.pop("resetTimeoutOnProgressNotification", UNSET)

        is_output_compression_enabled = d.pop("isOutputCompressionEnabled", UNSET)

        is_output_compression_transform_enabled = d.pop("isOutputCompressionTransformEnabled", UNSET)

        output_compression_threshold_bytes = d.pop("outputCompressionThresholdBytes", UNSET)

        _firewall_rules = d.pop("firewallRules", UNSET)
        firewall_rules: list[Schema58Item] | Unset = UNSET
        if _firewall_rules is not UNSET:
            firewall_rules = []
            for componentsschemas_schema58_item_data in _firewall_rules:
                componentsschemas_schema58_item = Schema58Item.from_dict(componentsschemas_schema58_item_data)

                firewall_rules.append(componentsschemas_schema58_item)

        _visibility = d.pop("visibility", UNSET)
        visibility: Schema59 | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Schema59(_visibility)

        update_server_request = cls(
            slug=slug,
            description=description,
            logo_url=logo_url,
            url=url,
            authorization=authorization,
            transport_config=transport_config,
            oauth_metadata=oauth_metadata,
            oauth_client_configuration=oauth_client_configuration,
            timeout_protocol=timeout_protocol,
            timeout_total=timeout_total,
            reset_timeout_on_progress_notification=reset_timeout_on_progress_notification,
            is_output_compression_enabled=is_output_compression_enabled,
            is_output_compression_transform_enabled=is_output_compression_transform_enabled,
            output_compression_threshold_bytes=output_compression_threshold_bytes,
            firewall_rules=firewall_rules,
            visibility=visibility,
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
