from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SandboxWithStatusDtoStatus")


@_attrs_define
class SandboxWithStatusDtoStatus:
    """
    Attributes:
        is_deployed (bool):
        is_available (bool):
        is_stabilizing (bool):
    """

    is_deployed: bool
    is_available: bool
    is_stabilizing: bool

    def to_dict(self) -> dict[str, Any]:
        is_deployed = self.is_deployed

        is_available = self.is_available

        is_stabilizing = self.is_stabilizing

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isDeployed": is_deployed,
                "isAvailable": is_available,
                "isStabilizing": is_stabilizing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_deployed = d.pop("isDeployed")

        is_available = d.pop("isAvailable")

        is_stabilizing = d.pop("isStabilizing")

        sandbox_with_status_dto_status = cls(
            is_deployed=is_deployed,
            is_available=is_available,
            is_stabilizing=is_stabilizing,
        )

        return sandbox_with_status_dto_status
