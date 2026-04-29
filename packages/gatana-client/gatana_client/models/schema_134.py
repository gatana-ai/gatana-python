from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_134_enabled_servers import Schema134EnabledServers


T = TypeVar("T", bound="Schema134")


@_attrs_define
class Schema134:
    """
    Attributes:
        enabled_servers (Schema134EnabledServers):
    """

    enabled_servers: Schema134EnabledServers

    def to_dict(self) -> dict[str, Any]:
        enabled_servers = self.enabled_servers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabledServers": enabled_servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_134_enabled_servers import Schema134EnabledServers

        d = dict(src_dict)
        enabled_servers = Schema134EnabledServers.from_dict(d.pop("enabledServers"))

        schema_134 = cls(
            enabled_servers=enabled_servers,
        )

        return schema_134
