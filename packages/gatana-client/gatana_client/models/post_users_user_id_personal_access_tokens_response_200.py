from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.personal_access_token import PersonalAccessToken


T = TypeVar("T", bound="PostUsersUserIdPersonalAccessTokensResponse200")


@_attrs_define
class PostUsersUserIdPersonalAccessTokensResponse200:
    """
    Attributes:
        token (PersonalAccessToken):
    """

    token: PersonalAccessToken

    def to_dict(self) -> dict[str, Any]:
        token = self.token.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.personal_access_token import PersonalAccessToken

        d = dict(src_dict)
        token = PersonalAccessToken.from_dict(d.pop("token"))

        post_users_user_id_personal_access_tokens_response_200 = cls(
            token=token,
        )

        return post_users_user_id_personal_access_tokens_response_200
