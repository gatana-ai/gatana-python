from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="Schema64")



@_attrs_define
class Schema64:
    """ 
        Attributes:
            success (bool):
            message (str):
     """

    success: bool
    message: str





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "success": success,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        schema_64 = cls(
            success=success,
            message=message,
        )

        return schema_64

