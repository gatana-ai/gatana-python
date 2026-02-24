from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sandbox_with_status_dto import SandboxWithStatusDto


T = TypeVar("T", bound="GetSandboxResponse")


@_attrs_define
class GetSandboxResponse:
    """
    Attributes:
        sandbox (SandboxWithStatusDto):
    """

    sandbox: SandboxWithStatusDto

    def to_dict(self) -> dict[str, Any]:
        sandbox = self.sandbox.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sandbox": sandbox,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_with_status_dto import SandboxWithStatusDto

        d = dict(src_dict)
        sandbox = SandboxWithStatusDto.from_dict(d.pop("sandbox"))

        get_sandbox_response = cls(
            sandbox=sandbox,
        )

        return get_sandbox_response
