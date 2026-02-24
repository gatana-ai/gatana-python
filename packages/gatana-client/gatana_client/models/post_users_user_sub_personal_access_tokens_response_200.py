from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.personal_access_token import PersonalAccessToken





T = TypeVar("T", bound="PostUsersUserSubPersonalAccessTokensResponse200")



@_attrs_define
class PostUsersUserSubPersonalAccessTokensResponse200:
    """ 
        Attributes:
            token (PersonalAccessToken):
     """

    token: PersonalAccessToken





    def to_dict(self) -> dict[str, Any]:
        from ..models.personal_access_token import PersonalAccessToken
        token = self.token.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "token": token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.personal_access_token import PersonalAccessToken
        d = dict(src_dict)
        token = PersonalAccessToken.from_dict(d.pop("token"))




        post_users_user_sub_personal_access_tokens_response_200 = cls(
            token=token,
        )

        return post_users_user_sub_personal_access_tokens_response_200

