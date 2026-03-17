from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schema_188 import Schema188
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostedTransportConfigOutput")


@_attrs_define
class HostedTransportConfigOutput:
    """
    Attributes:
        type_ (Literal['hosted']):
        runtime (Schema188):
        env (list[list[str]] | Unset):
    """

    type_: Literal["hosted"]
    runtime: Schema188
    env: list[list[str]] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        runtime = self.runtime.value

        env: list[list[str]] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for componentsschemas_schema189_item_data in self.env:
                componentsschemas_schema189_item = []
                for componentsschemas_schema189_item_item_data in componentsschemas_schema189_item_data:
                    componentsschemas_schema189_item_item: str
                    componentsschemas_schema189_item_item = componentsschemas_schema189_item_item_data
                    componentsschemas_schema189_item.append(componentsschemas_schema189_item_item)

                env.append(componentsschemas_schema189_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "runtime": runtime,
            }
        )
        if env is not UNSET:
            field_dict["env"] = env

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["hosted"], d.pop("type"))
        if type_ != "hosted":
            raise ValueError(f"type must match const 'hosted', got '{type_}'")

        runtime = Schema188(d.pop("runtime"))

        _env = d.pop("env", UNSET)
        env: list[list[str]] | Unset = UNSET
        if _env is not UNSET:
            env = []
            for componentsschemas_schema189_item_data in _env:
                componentsschemas_schema189_item = []
                _componentsschemas_schema189_item = componentsschemas_schema189_item_data
                for componentsschemas_schema189_item_item_data in _componentsschemas_schema189_item:

                    def _parse_componentsschemas_schema189_item_item(data: object) -> str:
                        return cast(str, data)

                    componentsschemas_schema189_item_item = _parse_componentsschemas_schema189_item_item(
                        componentsschemas_schema189_item_item_data
                    )

                    componentsschemas_schema189_item.append(componentsschemas_schema189_item_item)

                env.append(componentsschemas_schema189_item)

        hosted_transport_config_output = cls(
            type_=type_,
            runtime=runtime,
            env=env,
        )

        return hosted_transport_config_output
