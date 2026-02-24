from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecCommandBody")


@_attrs_define
class ExecCommandBody:
    """
    Attributes:
        command (str):
        workdir (str | Unset):
        timeout (float | Unset):
    """

    command: str
    workdir: str | Unset = UNSET
    timeout: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        workdir = self.workdir

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
            }
        )
        if workdir is not UNSET:
            field_dict["workdir"] = workdir
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command = d.pop("command")

        workdir = d.pop("workdir", UNSET)

        timeout = d.pop("timeout", UNSET)

        exec_command_body = cls(
            command=command,
            workdir=workdir,
            timeout=timeout,
        )

        exec_command_body.additional_properties = d
        return exec_command_body

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
