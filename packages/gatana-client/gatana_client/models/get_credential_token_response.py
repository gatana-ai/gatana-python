from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.get_credential_token_response_type import GetCredentialTokenResponseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCredentialTokenResponse")


@_attrs_define
class GetCredentialTokenResponse:
    """
    Attributes:
        type_ (GetCredentialTokenResponseType):
        access_token (str | Unset): The OAuth access token (refreshed if necessary and possible).
        expires_at (float | Unset): Unix timestamp (ms) when the access token expires.
        apikeys (list[list[str]] | Unset): Array of [key, value] tuples for API key credentials.
    """

    type_: GetCredentialTokenResponseType
    access_token: str | Unset = UNSET
    expires_at: float | Unset = UNSET
    apikeys: list[list[str]] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        access_token = self.access_token

        expires_at = self.expires_at

        apikeys: list[list[str]] | Unset = UNSET
        if not isinstance(self.apikeys, Unset):
            apikeys = []
            for apikeys_item_data in self.apikeys:
                apikeys_item = []
                for apikeys_item_item_data in apikeys_item_data:
                    apikeys_item_item: str
                    apikeys_item_item = apikeys_item_item_data
                    apikeys_item.append(apikeys_item_item)

                apikeys.append(apikeys_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if apikeys is not UNSET:
            field_dict["apikeys"] = apikeys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = GetCredentialTokenResponseType(d.pop("type"))

        access_token = d.pop("accessToken", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        _apikeys = d.pop("apikeys", UNSET)
        apikeys: list[list[str]] | Unset = UNSET
        if _apikeys is not UNSET:
            apikeys = []
            for apikeys_item_data in _apikeys:
                apikeys_item = []
                _apikeys_item = apikeys_item_data
                for apikeys_item_item_data in _apikeys_item:

                    def _parse_apikeys_item_item(data: object) -> str:
                        return cast(str, data)

                    apikeys_item_item = _parse_apikeys_item_item(apikeys_item_item_data)

                    apikeys_item.append(apikeys_item_item)

                apikeys.append(apikeys_item)

        get_credential_token_response = cls(
            type_=type_,
            access_token=access_token,
            expires_at=expires_at,
            apikeys=apikeys,
        )

        return get_credential_token_response
