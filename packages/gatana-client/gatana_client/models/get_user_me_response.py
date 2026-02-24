from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.get_user_me_response_user import GetUserMeResponseUser
    from ..models.user_identity import UserIdentity


T = TypeVar("T", bound="GetUserMeResponse")


@_attrs_define
class GetUserMeResponse:
    """
    Attributes:
        user (GetUserMeResponseUser):
        identities (list[UserIdentity]):
    """

    user: GetUserMeResponseUser
    identities: list[UserIdentity]

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        identities = []
        for identities_item_data in self.identities:
            identities_item = identities_item_data.to_dict()
            identities.append(identities_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "user": user,
                "identities": identities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_user_me_response_user import GetUserMeResponseUser
        from ..models.user_identity import UserIdentity

        d = dict(src_dict)
        user = GetUserMeResponseUser.from_dict(d.pop("user"))

        identities = []
        _identities = d.pop("identities")
        for identities_item_data in _identities:
            identities_item = UserIdentity.from_dict(identities_item_data)

            identities.append(identities_item)

        get_user_me_response = cls(
            user=user,
            identities=identities,
        )

        return get_user_me_response
