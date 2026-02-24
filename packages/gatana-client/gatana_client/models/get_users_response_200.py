from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.user import User





T = TypeVar("T", bound="GetUsersResponse200")



@_attrs_define
class GetUsersResponse200:
    """ 
        Attributes:
            users (list[User]):
     """

    users: list[User]





    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "users": users,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        d = dict(src_dict)
        users = []
        _users = d.pop("users")
        for users_item_data in (_users):
            users_item = User.from_dict(users_item_data)



            users.append(users_item)


        get_users_response_200 = cls(
            users=users,
        )

        return get_users_response_200

