from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AuthMetadataQuotaEnabledServers")



@_attrs_define
class AuthMetadataQuotaEnabledServers:
    """ 
        Attributes:
            quota (float):
            current (float):
            remaining (float):
     """

    quota: float
    current: float
    remaining: float





    def to_dict(self) -> dict[str, Any]:
        quota = self.quota

        current = self.current

        remaining = self.remaining


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "quota": quota,
            "current": current,
            "remaining": remaining,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quota = d.pop("quota")

        current = d.pop("current")

        remaining = d.pop("remaining")

        auth_metadata_quota_enabled_servers = cls(
            quota=quota,
            current=current,
            remaining=remaining,
        )

        return auth_metadata_quota_enabled_servers

