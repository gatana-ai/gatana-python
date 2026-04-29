from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schema_207 import Schema207
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_209_type_0 import Schema209Type0


T = TypeVar("T", bound="HostedTransportConfigOutput")


@_attrs_define
class HostedTransportConfigOutput:
    """
    Attributes:
        type_ (Literal['hosted']):
        runtime (Schema207):
        env (list[list[str]] | Unset):
        limits (None | Schema209Type0 | Unset):
    """

    type_: Literal["hosted"]
    runtime: Schema207
    env: list[list[str]] | Unset = UNSET
    limits: None | Schema209Type0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_209_type_0 import Schema209Type0

        type_ = self.type_

        runtime = self.runtime.value

        env: list[list[str]] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for componentsschemas_schema208_item_data in self.env:
                componentsschemas_schema208_item = []
                for componentsschemas_schema208_item_item_data in componentsschemas_schema208_item_data:
                    componentsschemas_schema208_item_item: str
                    componentsschemas_schema208_item_item = componentsschemas_schema208_item_item_data
                    componentsschemas_schema208_item.append(componentsschemas_schema208_item_item)

                env.append(componentsschemas_schema208_item)

        limits: dict[str, Any] | None | Unset
        if isinstance(self.limits, Unset):
            limits = UNSET
        elif isinstance(self.limits, Schema209Type0):
            limits = self.limits.to_dict()
        else:
            limits = self.limits

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "runtime": runtime,
            }
        )
        if env is not UNSET:
            field_dict["env"] = env
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_209_type_0 import Schema209Type0

        d = dict(src_dict)
        type_ = cast(Literal["hosted"], d.pop("type"))
        if type_ != "hosted":
            raise ValueError(f"type must match const 'hosted', got '{type_}'")

        runtime = Schema207(d.pop("runtime"))

        _env = d.pop("env", UNSET)
        env: list[list[str]] | Unset = UNSET
        if _env is not UNSET:
            env = []
            for componentsschemas_schema208_item_data in _env:
                componentsschemas_schema208_item = []
                _componentsschemas_schema208_item = componentsschemas_schema208_item_data
                for componentsschemas_schema208_item_item_data in _componentsschemas_schema208_item:

                    def _parse_componentsschemas_schema208_item_item(data: object) -> str:
                        return cast(str, data)

                    componentsschemas_schema208_item_item = _parse_componentsschemas_schema208_item_item(
                        componentsschemas_schema208_item_item_data
                    )

                    componentsschemas_schema208_item.append(componentsschemas_schema208_item_item)

                env.append(componentsschemas_schema208_item)

        def _parse_limits(data: object) -> None | Schema209Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema209_type_0 = Schema209Type0.from_dict(data)

                return componentsschemas_schema209_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Schema209Type0 | Unset, data)

        limits = _parse_limits(d.pop("limits", UNSET))

        hosted_transport_config_output = cls(
            type_=type_,
            runtime=runtime,
            env=env,
            limits=limits,
        )

        return hosted_transport_config_output
