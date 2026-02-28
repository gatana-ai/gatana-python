from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DeploymentLogPayloadType2")


@_attrs_define
class DeploymentLogPayloadType2:
    """
    Attributes:
        type_ (Literal['initContainerRunning']):
        name (str):
    """

    type_: Literal["initContainerRunning"]
    name: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["initContainerRunning"], d.pop("type"))
        if type_ != "initContainerRunning":
            raise ValueError(f"type must match const 'initContainerRunning', got '{type_}'")

        name = d.pop("name")

        deployment_log_payload_type_2 = cls(
            type_=type_,
            name=name,
        )

        return deployment_log_payload_type_2
