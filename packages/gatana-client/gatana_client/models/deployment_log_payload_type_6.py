from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DeploymentLogPayloadType6")


@_attrs_define
class DeploymentLogPayloadType6:
    """
    Attributes:
        type_ (Literal['mainContainerRunning']):
    """

    type_: Literal["mainContainerRunning"]

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["mainContainerRunning"], d.pop("type"))
        if type_ != "mainContainerRunning":
            raise ValueError(f"type must match const 'mainContainerRunning', got '{type_}'")

        deployment_log_payload_type_6 = cls(
            type_=type_,
        )

        return deployment_log_payload_type_6
