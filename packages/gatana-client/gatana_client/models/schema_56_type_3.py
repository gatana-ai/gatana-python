from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="Schema56Type3")



@_attrs_define
class Schema56Type3:
    """ 
        Attributes:
            type_ (Literal['self']):
            id (str):
     """

    type_: Literal['self']
    id: str





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['self'] , d.pop("type"))
        if type_ != 'self':
            raise ValueError(f"type must match const 'self', got '{type_}'")

        id = d.pop("id")

        schema_56_type_3 = cls(
            type_=type_,
            id=id,
        )

        return schema_56_type_3

