from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.personal_access_token import PersonalAccessToken





T = TypeVar("T", bound="GetUsersUserSubPersonalAccessTokensResponse200")



@_attrs_define
class GetUsersUserSubPersonalAccessTokensResponse200:
    """ 
        Attributes:
            tokens (list[PersonalAccessToken]):
     """

    tokens: list[PersonalAccessToken]





    def to_dict(self) -> dict[str, Any]:
        from ..models.personal_access_token import PersonalAccessToken
        tokens = []
        for tokens_item_data in self.tokens:
            tokens_item = tokens_item_data.to_dict()
            tokens.append(tokens_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tokens": tokens,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.personal_access_token import PersonalAccessToken
        d = dict(src_dict)
        tokens = []
        _tokens = d.pop("tokens")
        for tokens_item_data in (_tokens):
            tokens_item = PersonalAccessToken.from_dict(tokens_item_data)



            tokens.append(tokens_item)


        get_users_user_sub_personal_access_tokens_response_200 = cls(
            tokens=tokens,
        )

        return get_users_user_sub_personal_access_tokens_response_200

