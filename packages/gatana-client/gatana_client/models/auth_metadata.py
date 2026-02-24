from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.auth_metadata_quota import AuthMetadataQuota
    from ..models.auth_metadata_tenant import AuthMetadataTenant
    from ..models.auth_metadata_user import AuthMetadataUser


T = TypeVar("T", bound="AuthMetadata")


@_attrs_define
class AuthMetadata:
    """
    Attributes:
        is_playground (bool):
        has_paid_subscription (bool):
        user (AuthMetadataUser):
        tenant (AuthMetadataTenant):
        rules (list[Any]):
        quota (AuthMetadataQuota):
    """

    is_playground: bool
    has_paid_subscription: bool
    user: AuthMetadataUser
    tenant: AuthMetadataTenant
    rules: list[Any]
    quota: AuthMetadataQuota

    def to_dict(self) -> dict[str, Any]:
        is_playground = self.is_playground

        has_paid_subscription = self.has_paid_subscription

        user = self.user.to_dict()

        tenant = self.tenant.to_dict()

        rules = self.rules

        quota = self.quota.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isPlayground": is_playground,
                "hasPaidSubscription": has_paid_subscription,
                "user": user,
                "tenant": tenant,
                "rules": rules,
                "quota": quota,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_metadata_quota import AuthMetadataQuota
        from ..models.auth_metadata_tenant import AuthMetadataTenant
        from ..models.auth_metadata_user import AuthMetadataUser

        d = dict(src_dict)
        is_playground = d.pop("isPlayground")

        has_paid_subscription = d.pop("hasPaidSubscription")

        user = AuthMetadataUser.from_dict(d.pop("user"))

        tenant = AuthMetadataTenant.from_dict(d.pop("tenant"))

        rules = cast(list[Any], d.pop("rules"))

        quota = AuthMetadataQuota.from_dict(d.pop("quota"))

        auth_metadata = cls(
            is_playground=is_playground,
            has_paid_subscription=has_paid_subscription,
            user=user,
            tenant=tenant,
            rules=rules,
            quota=quota,
        )

        return auth_metadata
