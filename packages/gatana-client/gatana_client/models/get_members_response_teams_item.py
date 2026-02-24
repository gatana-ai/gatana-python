from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.schema_65 import Schema65






T = TypeVar("T", bound="GetMembersResponseTeamsItem")



@_attrs_define
class GetMembersResponseTeamsItem:
    """ 
        Attributes:
            role (Schema65):
            id (str):
            name (str):
     """

    role: Schema65
    id: str
    name: str





    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "role": role,
            "id": id,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = Schema65(d.pop("role"))




        id = d.pop("id")

        name = d.pop("name")

        get_members_response_teams_item = cls(
            role=role,
            id=id,
            name=name,
        )

        return get_members_response_teams_item

