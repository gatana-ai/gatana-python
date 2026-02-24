from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AuthMetadataTenantAbilities")


@_attrs_define
class AuthMetadataTenantAbilities:
    """
    Attributes:
        can_have_multiple_users (bool):
        can_use_sandbox (bool):
        can_use_hosted_servers (bool):
        can_use_local_servers (bool):
        can_update_seats (bool):
        max_enabled_servers (float):
        max_users (float):
        has_paid_features (bool):
    """

    can_have_multiple_users: bool
    can_use_sandbox: bool
    can_use_hosted_servers: bool
    can_use_local_servers: bool
    can_update_seats: bool
    max_enabled_servers: float
    max_users: float
    has_paid_features: bool

    def to_dict(self) -> dict[str, Any]:
        can_have_multiple_users = self.can_have_multiple_users

        can_use_sandbox = self.can_use_sandbox

        can_use_hosted_servers = self.can_use_hosted_servers

        can_use_local_servers = self.can_use_local_servers

        can_update_seats = self.can_update_seats

        max_enabled_servers = self.max_enabled_servers

        max_users = self.max_users

        has_paid_features = self.has_paid_features

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "canHaveMultipleUsers": can_have_multiple_users,
                "canUseSandbox": can_use_sandbox,
                "canUseHostedServers": can_use_hosted_servers,
                "canUseLocalServers": can_use_local_servers,
                "canUpdateSeats": can_update_seats,
                "maxEnabledServers": max_enabled_servers,
                "maxUsers": max_users,
                "hasPaidFeatures": has_paid_features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_have_multiple_users = d.pop("canHaveMultipleUsers")

        can_use_sandbox = d.pop("canUseSandbox")

        can_use_hosted_servers = d.pop("canUseHostedServers")

        can_use_local_servers = d.pop("canUseLocalServers")

        can_update_seats = d.pop("canUpdateSeats")

        max_enabled_servers = d.pop("maxEnabledServers")

        max_users = d.pop("maxUsers")

        has_paid_features = d.pop("hasPaidFeatures")

        auth_metadata_tenant_abilities = cls(
            can_have_multiple_users=can_have_multiple_users,
            can_use_sandbox=can_use_sandbox,
            can_use_hosted_servers=can_use_hosted_servers,
            can_use_local_servers=can_use_local_servers,
            can_update_seats=can_update_seats,
            max_enabled_servers=max_enabled_servers,
            max_users=max_users,
            has_paid_features=has_paid_features,
        )

        return auth_metadata_tenant_abilities
