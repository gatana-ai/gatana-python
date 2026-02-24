from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostSandboxesSandboxIdExecResponse200")


@_attrs_define
class PostSandboxesSandboxIdExecResponse200:
    """ """

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        post_sandboxes_sandbox_id_exec_response_200 = cls()

        return post_sandboxes_sandbox_id_exec_response_200
