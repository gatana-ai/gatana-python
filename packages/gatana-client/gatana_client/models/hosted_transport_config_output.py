from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hosted_transport_config_output_runtime import HostedTransportConfigOutputRuntime
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="HostedTransportConfigOutput")



@_attrs_define
class HostedTransportConfigOutput:
    """ 
        Attributes:
            type_ (Literal['hosted']):
            runtime (HostedTransportConfigOutputRuntime):
            env (list[list[str]] | Unset):
     """

    type_: Literal['hosted']
    runtime: HostedTransportConfigOutputRuntime
    env: list[list[str]] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        runtime = self.runtime.value

        env: list[list[str]] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for env_item_data in self.env:
                env_item = []
                for env_item_item_data in env_item_data:
                    env_item_item: str
                    env_item_item = env_item_item_data
                    env_item.append(env_item_item)


                env.append(env_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "runtime": runtime,
        })
        if env is not UNSET:
            field_dict["env"] = env

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['hosted'] , d.pop("type"))
        if type_ != 'hosted':
            raise ValueError(f"type must match const 'hosted', got '{type_}'")

        runtime = HostedTransportConfigOutputRuntime(d.pop("runtime"))




        _env = d.pop("env", UNSET)
        env: list[list[str]] | Unset = UNSET
        if _env is not UNSET:
            env = []
            for env_item_data in _env:
                env_item = []
                _env_item = env_item_data
                for env_item_item_data in (_env_item):
                    def _parse_env_item_item(data: object) -> str:
                        return cast(str, data)

                    env_item_item = _parse_env_item_item(env_item_item_data)

                    env_item.append(env_item_item)

                env.append(env_item)


        hosted_transport_config_output = cls(
            type_=type_,
            runtime=runtime,
            env=env,
        )

        return hosted_transport_config_output

