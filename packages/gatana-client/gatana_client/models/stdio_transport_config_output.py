from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schema_181 import Schema181
from ..types import UNSET, Unset

T = TypeVar("T", bound="StdioTransportConfigOutput")


@_attrs_define
class StdioTransportConfigOutput:
    """
    Attributes:
        type_ (Literal['stdio']):
        command (str):
        transport (Schema181):
        docker_image (str | Unset):
        env (list[list[str]] | Unset):
        http_port (float | None | Unset):
        url_path (None | str | Unset):
    """

    type_: Literal["stdio"]
    command: str
    transport: Schema181
    docker_image: str | Unset = UNSET
    env: list[list[str]] | Unset = UNSET
    http_port: float | None | Unset = UNSET
    url_path: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        command = self.command

        transport = self.transport.value

        docker_image = self.docker_image

        env: list[list[str]] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for componentsschemas_schema180_item_data in self.env:
                componentsschemas_schema180_item = []
                for componentsschemas_schema180_item_item_data in componentsschemas_schema180_item_data:
                    componentsschemas_schema180_item_item: str
                    componentsschemas_schema180_item_item = componentsschemas_schema180_item_item_data
                    componentsschemas_schema180_item.append(componentsschemas_schema180_item_item)

                env.append(componentsschemas_schema180_item)

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

        field_dict: dict[str, Any] = {}

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["stdio"], d.pop("type"))
        if type_ != "stdio":
            raise ValueError(f"type must match const 'stdio', got '{type_}'")

        command = d.pop("command")

        transport = Schema181(d.pop("transport"))

        docker_image = d.pop("dockerImage", UNSET)

        _env = d.pop("env", UNSET)
        env: list[list[str]] | Unset = UNSET
        if _env is not UNSET:
            env = []
            for componentsschemas_schema180_item_data in _env:
                componentsschemas_schema180_item = []
                _componentsschemas_schema180_item = componentsschemas_schema180_item_data
                for componentsschemas_schema180_item_item_data in _componentsschemas_schema180_item:

                    def _parse_componentsschemas_schema180_item_item(data: object) -> str:
                        return cast(str, data)

                    componentsschemas_schema180_item_item = _parse_componentsschemas_schema180_item_item(
                        componentsschemas_schema180_item_item_data
                    )

                    componentsschemas_schema180_item.append(componentsschemas_schema180_item_item)

                env.append(componentsschemas_schema180_item)

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

        stdio_transport_config_output = cls(
            type_=type_,
            command=command,
            transport=transport,
            docker_image=docker_image,
            env=env,
            http_port=http_port,
            url_path=url_path,
        )

        return stdio_transport_config_output
