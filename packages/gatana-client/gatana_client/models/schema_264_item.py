from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schema_129 import Schema129

T = TypeVar("T", bound="Schema264Item")


@_attrs_define
class Schema264Item:
    """
    Attributes:
        role (Schema129):
        id (str):
        name (str):
        email (str):
    """

    role: Schema129
    id: str
    name: str
    email: str

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        id = self.id

        name = self.name

        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
                "id": id,
                "name": name,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = Schema129(d.pop("role"))

        id = d.pop("id")

        name = d.pop("name")

        email = d.pop("email")

        schema_264_item = cls(
            role=role,
            id=id,
            name=name,
            email=email,
        )

        return schema_264_item
