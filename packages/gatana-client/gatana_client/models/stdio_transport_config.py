from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schema_53 import Schema53
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_56_type_0 import Schema56Type0


T = TypeVar("T", bound="StdioTransportConfig")


@_attrs_define
class StdioTransportConfig:
    """
    Attributes:
        type_ (Literal['stdio']):
        command (str):
        transport (Schema53):
        docker_image (str | Unset):
        env (list[list[str]] | Unset):
        http_port (float | None | Unset):
        url_path (None | str | Unset):
        limits (None | Schema56Type0 | Unset):
    """

    type_: Literal["stdio"]
    command: str
    transport: Schema53
    docker_image: str | Unset = UNSET
    env: list[list[str]] | Unset = UNSET
    http_port: float | None | Unset = UNSET
    url_path: None | str | Unset = UNSET
    limits: None | Schema56Type0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_56_type_0 import Schema56Type0

        type_ = self.type_

        command = self.command

        transport = self.transport.value

        docker_image = self.docker_image

        env: list[list[str]] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for componentsschemas_schema52_item_data in self.env:
                componentsschemas_schema52_item = []
                for componentsschemas_schema52_item_item_data in componentsschemas_schema52_item_data:
                    componentsschemas_schema52_item_item: str
                    componentsschemas_schema52_item_item = componentsschemas_schema52_item_item_data
                    componentsschemas_schema52_item.append(componentsschemas_schema52_item_item)

                env.append(componentsschemas_schema52_item)

        http_port: float | None | Unset
        if isinstance(self.http_port, Unset):
            http_port = UNSET
        else:
            http_port = self.http_port

        url_path: None | str | Unset
        if isinstance(self.url_path, Unset):
            url_path = UNSET
        else:
            url_path = self.url_path

        limits: dict[str, Any] | None | Unset
        if isinstance(self.limits, Unset):
            limits = UNSET
        elif isinstance(self.limits, Schema56Type0):
            limits = self.limits.to_dict()
        else:
            limits = self.limits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "command": command,
                "transport": transport,
            }
        )
        if docker_image is not UNSET:
            field_dict["dockerImage"] = docker_image
        if env is not UNSET:
            field_dict["env"] = env
        if http_port is not UNSET:
            field_dict["httpPort"] = http_port
        if url_path is not UNSET:
            field_dict["urlPath"] = url_path
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_56_type_0 import Schema56Type0

        d = dict(src_dict)
        type_ = cast(Literal["stdio"], d.pop("type"))
        if type_ != "stdio":
            raise ValueError(f"type must match const 'stdio', got '{type_}'")

        command = d.pop("command")

        transport = Schema53(d.pop("transport"))

        docker_image = d.pop("dockerImage", UNSET)

        _env = d.pop("env", UNSET)
        env: list[list[str]] | Unset = UNSET
        if _env is not UNSET:
            env = []
            for componentsschemas_schema52_item_data in _env:
                componentsschemas_schema52_item = []
                _componentsschemas_schema52_item = componentsschemas_schema52_item_data
                for componentsschemas_schema52_item_item_data in _componentsschemas_schema52_item:

                    def _parse_componentsschemas_schema52_item_item(data: object) -> str:
                        return cast(str, data)

                    componentsschemas_schema52_item_item = _parse_componentsschemas_schema52_item_item(
                        componentsschemas_schema52_item_item_data
                    )

                    componentsschemas_schema52_item.append(componentsschemas_schema52_item_item)

                env.append(componentsschemas_schema52_item)

        def _parse_http_port(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        http_port = _parse_http_port(d.pop("httpPort", UNSET))

        def _parse_url_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_path = _parse_url_path(d.pop("urlPath", UNSET))

        def _parse_limits(data: object) -> None | Schema56Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema56_type_0 = Schema56Type0.from_dict(data)

                return componentsschemas_schema56_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Schema56Type0 | Unset, data)

        limits = _parse_limits(d.pop("limits", UNSET))

        stdio_transport_config = cls(
            type_=type_,
            command=command,
            transport=transport,
            docker_image=docker_image,
            env=env,
            http_port=http_port,
            url_path=url_path,
            limits=limits,
        )

        stdio_transport_config.additional_properties = d
        return stdio_transport_config

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
