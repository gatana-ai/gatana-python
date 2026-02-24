from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schema_66 import Schema66

T = TypeVar("T", bound="GetMembersResponseUsersItem")


@_attrs_define
class GetMembersResponseUsersItem:
    """
    Attributes:
        role (Schema66):
        sub (str):
        name (str):
        email (str):
    """

    role: Schema66
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
        role = Schema66(d.pop("role"))

        sub = d.pop("sub")

        name = d.pop("name")

        email = d.pop("email")

        get_members_response_users_item = cls(
            role=role,
            sub=sub,
            name=name,
            email=email,
        )

        return get_members_response_users_item
