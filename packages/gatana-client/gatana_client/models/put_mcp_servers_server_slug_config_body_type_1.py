from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.schema_11 import Schema11
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="PutMcpServersServerSlugConfigBodyType1")



@_attrs_define
class PutMcpServersServerSlugConfigBodyType1:
    """ 
        Attributes:
            type_ (Literal['hosted'] | Unset):
            runtime (Schema11 | Unset):
            env (list[list[str]] | Unset):
     """

    type_: Literal['hosted'] | Unset = UNSET
    runtime: Schema11 | Unset = UNSET
    env: list[list[str]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        runtime: str | Unset = UNSET
        if not isinstance(self.runtime, Unset):
            runtime = self.runtime.value


        env: list[list[str]] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for componentsschemas_schema12_item_data in self.env:
                componentsschemas_schema12_item = []
                for componentsschemas_schema12_item_item_data in componentsschemas_schema12_item_data:
                    componentsschemas_schema12_item_item: str
                    componentsschemas_schema12_item_item = componentsschemas_schema12_item_item_data
                    componentsschemas_schema12_item.append(componentsschemas_schema12_item_item)


                env.append(componentsschemas_schema12_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if env is not UNSET:
            field_dict["env"] = env

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['hosted'] | Unset , d.pop("type", UNSET))
        if type_ != 'hosted'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'hosted', got '{type_}'")

        _runtime = d.pop("runtime", UNSET)
        runtime: Schema11 | Unset
        if isinstance(_runtime,  Unset):
            runtime = UNSET
        else:
            runtime = Schema11(_runtime)




        _env = d.pop("env", UNSET)
        env: list[list[str]] | Unset = UNSET
        if _env is not UNSET:
            env = []
            for componentsschemas_schema12_item_data in _env:
                componentsschemas_schema12_item = []
                _componentsschemas_schema12_item = componentsschemas_schema12_item_data
                for componentsschemas_schema12_item_item_data in (_componentsschemas_schema12_item):
                    def _parse_componentsschemas_schema12_item_item(data: object) -> str:
                        return cast(str, data)

                    componentsschemas_schema12_item_item = _parse_componentsschemas_schema12_item_item(componentsschemas_schema12_item_item_data)

                    componentsschemas_schema12_item.append(componentsschemas_schema12_item_item)

                env.append(componentsschemas_schema12_item)


        put_mcp_servers_server_slug_config_body_type_1 = cls(
            type_=type_,
            runtime=runtime,
            env=env,
        )


        put_mcp_servers_server_slug_config_body_type_1.additional_properties = d
        return put_mcp_servers_server_slug_config_body_type_1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
