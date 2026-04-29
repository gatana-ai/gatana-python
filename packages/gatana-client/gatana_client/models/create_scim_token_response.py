from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.scim_token import ScimToken


T = TypeVar("T", bound="CreateScimTokenResponse")


@_attrs_define
class CreateScimTokenResponse:
    """
    Attributes:
        token (ScimToken):
        raw_token (str):
    """

    token: ScimToken
    raw_token: str

    def to_dict(self) -> dict[str, Any]:
        token = self.token.to_dict()

        raw_token = self.raw_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "token": token,
                "rawToken": raw_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scim_token import ScimToken

        d = dict(src_dict)
        token = ScimToken.from_dict(d.pop("token"))

        raw_token = d.pop("rawToken")

        create_scim_token_response = cls(
            token=token,
            raw_token=raw_token,
        )

        return create_scim_token_response
