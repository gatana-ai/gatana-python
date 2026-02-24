from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.auth_metadata_quota_enabled_servers import AuthMetadataQuotaEnabledServers





T = TypeVar("T", bound="AuthMetadataQuota")



@_attrs_define
class AuthMetadataQuota:
    """ 
        Attributes:
            enabled_servers (AuthMetadataQuotaEnabledServers):
     """

    enabled_servers: AuthMetadataQuotaEnabledServers





    def to_dict(self) -> dict[str, Any]:
        from ..models.auth_metadata_quota_enabled_servers import AuthMetadataQuotaEnabledServers
        enabled_servers = self.enabled_servers.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "enabledServers": enabled_servers,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_metadata_quota_enabled_servers import AuthMetadataQuotaEnabledServers
        d = dict(src_dict)
        enabled_servers = AuthMetadataQuotaEnabledServers.from_dict(d.pop("enabledServers"))




        auth_metadata_quota = cls(
            enabled_servers=enabled_servers,
        )

        return auth_metadata_quota

