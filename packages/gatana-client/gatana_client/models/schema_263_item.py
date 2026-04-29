from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schema_129 import Schema129

T = TypeVar("T", bound="Schema263Item")


@_attrs_define
class Schema263Item:
    """
    Attributes:
        role (Schema129):
        id (str):
        name (str):
    """

    role: Schema129
    id: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = Schema129(d.pop("role"))

        id = d.pop("id")

        name = d.pop("name")

        schema_263_item = cls(
            role=role,
            id=id,
            name=name,
        )

        return schema_263_item
