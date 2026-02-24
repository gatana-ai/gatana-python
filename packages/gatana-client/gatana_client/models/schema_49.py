from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.user import User





T = TypeVar("T", bound="Schema49")



@_attrs_define
class Schema49:
    """ 
        Attributes:
            user (User):
     """

    user: User





    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User
        user = self.user.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "user": user,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        d = dict(src_dict)
        user = User.from_dict(d.pop("user"))




        schema_49 = cls(
            user=user,
        )

        return schema_49

