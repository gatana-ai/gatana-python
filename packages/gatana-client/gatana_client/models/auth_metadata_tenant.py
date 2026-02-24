from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_metadata_tenant_abilities import AuthMetadataTenantAbilities


T = TypeVar("T", bound="AuthMetadataTenant")


@_attrs_define
class AuthMetadataTenant:
    """
    Attributes:
        id (str):
        is_mcp_authorization_api_key_enabled (bool):
        grant_users_install_servers_policy (bool):
        display_name (str):
        is_trial (bool):
        subscription_plan (str):
        subscription_seats (float):
        free_credits (float):
        paid_credits (float):
        abilities (AuthMetadataTenantAbilities):
        number_of_enabled_users (float | Unset):
    """

    id: str
    is_mcp_authorization_api_key_enabled: bool
    grant_users_install_servers_policy: bool
    display_name: str
    is_trial: bool
    subscription_plan: str
    subscription_seats: float
    free_credits: float
    paid_credits: float
    abilities: AuthMetadataTenantAbilities
    number_of_enabled_users: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_mcp_authorization_api_key_enabled = self.is_mcp_authorization_api_key_enabled

        grant_users_install_servers_policy = self.grant_users_install_servers_policy

        display_name = self.display_name

        is_trial = self.is_trial

        subscription_plan = self.subscription_plan

        subscription_seats = self.subscription_seats

        free_credits = self.free_credits

        paid_credits = self.paid_credits

        abilities = self.abilities.to_dict()

        number_of_enabled_users = self.number_of_enabled_users

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "isMcpAuthorizationApiKeyEnabled": is_mcp_authorization_api_key_enabled,
                "grantUsersInstallServersPolicy": grant_users_install_servers_policy,
                "displayName": display_name,
                "isTrial": is_trial,
                "subscriptionPlan": subscription_plan,
                "subscriptionSeats": subscription_seats,
                "freeCredits": free_credits,
                "paidCredits": paid_credits,
                "abilities": abilities,
            }
        )
        if number_of_enabled_users is not UNSET:
            field_dict["numberOfEnabledUsers"] = number_of_enabled_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_metadata_tenant_abilities import AuthMetadataTenantAbilities

        d = dict(src_dict)
        id = d.pop("id")

        is_mcp_authorization_api_key_enabled = d.pop("isMcpAuthorizationApiKeyEnabled")

        grant_users_install_servers_policy = d.pop("grantUsersInstallServersPolicy")

        display_name = d.pop("displayName")

        is_trial = d.pop("isTrial")

        subscription_plan = d.pop("subscriptionPlan")

        subscription_seats = d.pop("subscriptionSeats")

        free_credits = d.pop("freeCredits")

        paid_credits = d.pop("paidCredits")

        abilities = AuthMetadataTenantAbilities.from_dict(d.pop("abilities"))

        number_of_enabled_users = d.pop("numberOfEnabledUsers", UNSET)

        auth_metadata_tenant = cls(
            id=id,
            is_mcp_authorization_api_key_enabled=is_mcp_authorization_api_key_enabled,
            grant_users_install_servers_policy=grant_users_install_servers_policy,
            display_name=display_name,
            is_trial=is_trial,
            subscription_plan=subscription_plan,
            subscription_seats=subscription_seats,
            free_credits=free_credits,
            paid_credits=paid_credits,
            abilities=abilities,
            number_of_enabled_users=number_of_enabled_users,
        )

        return auth_metadata_tenant
