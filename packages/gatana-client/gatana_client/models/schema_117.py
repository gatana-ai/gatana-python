from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_117_abilities import Schema117Abilities


T = TypeVar("T", bound="Schema117")


@_attrs_define
class Schema117:
    """
    Attributes:
        id (str):
        is_mcp_authorization_api_key_enabled (bool):
        is_output_compression_allowed (bool):
        grant_users_install_servers_policy (bool):
        display_name (str):
        is_trial (bool):
        subscription_plan (str):
        subscription_seats (float):
        free_credits (float):
        paid_credits (float):
        abilities (Schema117Abilities):
        number_of_enabled_users (float | Unset):
    """

    id: str
    is_mcp_authorization_api_key_enabled: bool
    is_output_compression_allowed: bool
    grant_users_install_servers_policy: bool
    display_name: str
    is_trial: bool
    subscription_plan: str
    subscription_seats: float
    free_credits: float
    paid_credits: float
    abilities: Schema117Abilities
    number_of_enabled_users: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_mcp_authorization_api_key_enabled = self.is_mcp_authorization_api_key_enabled

        is_output_compression_allowed = self.is_output_compression_allowed

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
                "isOutputCompressionAllowed": is_output_compression_allowed,
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
        from ..models.schema_117_abilities import Schema117Abilities

        d = dict(src_dict)
        id = d.pop("id")

        is_mcp_authorization_api_key_enabled = d.pop("isMcpAuthorizationApiKeyEnabled")

        is_output_compression_allowed = d.pop("isOutputCompressionAllowed")

        grant_users_install_servers_policy = d.pop("grantUsersInstallServersPolicy")

        display_name = d.pop("displayName")

        is_trial = d.pop("isTrial")

        subscription_plan = d.pop("subscriptionPlan")

        subscription_seats = d.pop("subscriptionSeats")

        free_credits = d.pop("freeCredits")

        paid_credits = d.pop("paidCredits")

        abilities = Schema117Abilities.from_dict(d.pop("abilities"))

        number_of_enabled_users = d.pop("numberOfEnabledUsers", UNSET)

        schema_117 = cls(
            id=id,
            is_mcp_authorization_api_key_enabled=is_mcp_authorization_api_key_enabled,
            is_output_compression_allowed=is_output_compression_allowed,
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

        return schema_117
