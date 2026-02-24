from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ServerToolDtoOutputSchemaType0")



@_attrs_define
class ServerToolDtoOutputSchemaType0:
    """ 
     """






    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        server_tool_dto_output_schema_type_0 = cls(
        )

        return server_tool_dto_output_schema_type_0

