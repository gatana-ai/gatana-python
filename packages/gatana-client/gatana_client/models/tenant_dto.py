from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mcp_audit_log_verbosity import McpAuditLogVerbosity
from ..models.schema_65 import Schema65
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.tenant_oidc_configuration import TenantOidcConfiguration
  from ..models.tenant_saml_configuration import TenantSamlConfiguration





T = TypeVar("T", bound="TenantDto")



@_attrs_define
class TenantDto:
    """ 
        Attributes:
            id (str):
            is_playground (bool):
            display_name (str):
            upstream_oidc_configuration (None | TenantOidcConfiguration):
            upstream_saml_configuration (None | TenantSamlConfiguration):
            is_upstream_oidc_tokens_trusted (bool):
            is_automatic_seat_increase_enabled (bool):
            is_mcp_authorization_api_key_enabled (bool):
            grant_permissions_new_tool_policy (bool):
            allow_member_add_remote_servers (bool):
            allow_member_add_local_servers (bool):
            allow_member_add_hosted_servers (bool):
            is_google_refresh_token_saving_enabled (bool):
            member_default_role (Literal['none'] | Schema65):
            mcp_audit_log_level (McpAuditLogVerbosity):
     """

    id: str
    is_playground: bool
    display_name: str
    upstream_oidc_configuration: None | TenantOidcConfiguration
    upstream_saml_configuration: None | TenantSamlConfiguration
    is_upstream_oidc_tokens_trusted: bool
    is_automatic_seat_increase_enabled: bool
    is_mcp_authorization_api_key_enabled: bool
    grant_permissions_new_tool_policy: bool
    allow_member_add_remote_servers: bool
    allow_member_add_local_servers: bool
    allow_member_add_hosted_servers: bool
    is_google_refresh_token_saving_enabled: bool
    member_default_role: Literal['none'] | Schema65
    mcp_audit_log_level: McpAuditLogVerbosity





    def to_dict(self) -> dict[str, Any]:
        from ..models.tenant_saml_configuration import TenantSamlConfiguration
        from ..models.tenant_oidc_configuration import TenantOidcConfiguration
        id = self.id

        is_playground = self.is_playground

        display_name = self.display_name

        upstream_oidc_configuration: dict[str, Any] | None
        if isinstance(self.upstream_oidc_configuration, TenantOidcConfiguration):
            upstream_oidc_configuration = self.upstream_oidc_configuration.to_dict()
        else:
            upstream_oidc_configuration = self.upstream_oidc_configuration

        upstream_saml_configuration: dict[str, Any] | None
        if isinstance(self.upstream_saml_configuration, TenantSamlConfiguration):
            upstream_saml_configuration = self.upstream_saml_configuration.to_dict()
        else:
            upstream_saml_configuration = self.upstream_saml_configuration

        is_upstream_oidc_tokens_trusted = self.is_upstream_oidc_tokens_trusted

        is_automatic_seat_increase_enabled = self.is_automatic_seat_increase_enabled

        is_mcp_authorization_api_key_enabled = self.is_mcp_authorization_api_key_enabled

        grant_permissions_new_tool_policy = self.grant_permissions_new_tool_policy

        allow_member_add_remote_servers = self.allow_member_add_remote_servers

        allow_member_add_local_servers = self.allow_member_add_local_servers

        allow_member_add_hosted_servers = self.allow_member_add_hosted_servers

        is_google_refresh_token_saving_enabled = self.is_google_refresh_token_saving_enabled

        member_default_role: Literal['none'] | str
        if isinstance(self.member_default_role, Schema65):
            member_default_role = self.member_default_role.value
        else:
            member_default_role = self.member_default_role

        mcp_audit_log_level = self.mcp_audit_log_level.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "isPlayground": is_playground,
            "displayName": display_name,
            "upstreamOidcConfiguration": upstream_oidc_configuration,
            "upstreamSamlConfiguration": upstream_saml_configuration,
            "isUpstreamOidcTokensTrusted": is_upstream_oidc_tokens_trusted,
            "isAutomaticSeatIncreaseEnabled": is_automatic_seat_increase_enabled,
            "isMcpAuthorizationApiKeyEnabled": is_mcp_authorization_api_key_enabled,
            "grantPermissionsNewToolPolicy": grant_permissions_new_tool_policy,
            "allowMemberAddRemoteServers": allow_member_add_remote_servers,
            "allowMemberAddLocalServers": allow_member_add_local_servers,
            "allowMemberAddHostedServers": allow_member_add_hosted_servers,
            "isGoogleRefreshTokenSavingEnabled": is_google_refresh_token_saving_enabled,
            "memberDefaultRole": member_default_role,
            "mcpAuditLogLevel": mcp_audit_log_level,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_oidc_configuration import TenantOidcConfiguration
        from ..models.tenant_saml_configuration import TenantSamlConfiguration
        d = dict(src_dict)
        id = d.pop("id")

        is_playground = d.pop("isPlayground")

        display_name = d.pop("displayName")

        def _parse_upstream_oidc_configuration(data: object) -> None | TenantOidcConfiguration:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upstream_oidc_configuration_type_0 = TenantOidcConfiguration.from_dict(data)



                return upstream_oidc_configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TenantOidcConfiguration, data)

        upstream_oidc_configuration = _parse_upstream_oidc_configuration(d.pop("upstreamOidcConfiguration"))


        def _parse_upstream_saml_configuration(data: object) -> None | TenantSamlConfiguration:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upstream_saml_configuration_type_0 = TenantSamlConfiguration.from_dict(data)



                return upstream_saml_configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TenantSamlConfiguration, data)

        upstream_saml_configuration = _parse_upstream_saml_configuration(d.pop("upstreamSamlConfiguration"))


        is_upstream_oidc_tokens_trusted = d.pop("isUpstreamOidcTokensTrusted")

        is_automatic_seat_increase_enabled = d.pop("isAutomaticSeatIncreaseEnabled")

        is_mcp_authorization_api_key_enabled = d.pop("isMcpAuthorizationApiKeyEnabled")

        grant_permissions_new_tool_policy = d.pop("grantPermissionsNewToolPolicy")

        allow_member_add_remote_servers = d.pop("allowMemberAddRemoteServers")

        allow_member_add_local_servers = d.pop("allowMemberAddLocalServers")

        allow_member_add_hosted_servers = d.pop("allowMemberAddHostedServers")

        is_google_refresh_token_saving_enabled = d.pop("isGoogleRefreshTokenSavingEnabled")

        def _parse_member_default_role(data: object) -> Literal['none'] | Schema65:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                member_default_role_type_0 = Schema65(data)



                return member_default_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            member_default_role_type_1 = cast(Literal['none'] , data)
            if member_default_role_type_1 != 'none':
                raise ValueError(f"memberDefaultRole_type_1 must match const 'none', got '{member_default_role_type_1}'")
            return member_default_role_type_1

        member_default_role = _parse_member_default_role(d.pop("memberDefaultRole"))


        mcp_audit_log_level = McpAuditLogVerbosity(d.pop("mcpAuditLogLevel"))




        tenant_dto = cls(
            id=id,
            is_playground=is_playground,
            display_name=display_name,
            upstream_oidc_configuration=upstream_oidc_configuration,
            upstream_saml_configuration=upstream_saml_configuration,
            is_upstream_oidc_tokens_trusted=is_upstream_oidc_tokens_trusted,
            is_automatic_seat_increase_enabled=is_automatic_seat_increase_enabled,
            is_mcp_authorization_api_key_enabled=is_mcp_authorization_api_key_enabled,
            grant_permissions_new_tool_policy=grant_permissions_new_tool_policy,
            allow_member_add_remote_servers=allow_member_add_remote_servers,
            allow_member_add_local_servers=allow_member_add_local_servers,
            allow_member_add_hosted_servers=allow_member_add_hosted_servers,
            is_google_refresh_token_saving_enabled=is_google_refresh_token_saving_enabled,
            member_default_role=member_default_role,
            mcp_audit_log_level=mcp_audit_log_level,
        )

        return tenant_dto

