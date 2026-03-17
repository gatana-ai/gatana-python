from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schema_244 import Schema244

T = TypeVar("T", bound="Schema245Item")


@_attrs_define
class Schema245Item:
    """
    Attributes:
        role (Schema244):
        sub (str):
        name (str):
        email (str):
    """

    role: Schema244
    sub: str
    name: str
    email: str

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        sub = self.sub

        name = self.name

        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
                "sub": sub,
                "name": name,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = Schema244(d.pop("role"))

        sub = d.pop("sub")

        name = d.pop("name")

        email = d.pop("email")

        schema_245_item = cls(
            role=role,
            sub=sub,
            name=name,
            email=email,
        )

        return schema_245_item
