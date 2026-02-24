from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schema_67 import Schema67
from ..models.server_credentials_dto_type import ServerCredentialsDtoType

T = TypeVar("T", bound="ServerCredentialsDto")


@_attrs_define
class ServerCredentialsDto:
    """
    Attributes:
        id (str):
        tenant_id (str):
        scope (Schema67):
        user_id (float | None):
        profile_id (None | str):
        last_used_at (None | str):
        authorized_at (str):
        type_ (ServerCredentialsDtoType):
        created_at (str):
        updated_at (str):
        user_sub (None | str):
        user_email (None | str):
        user_name (None | str):
        profile_name (None | str):
        apikeys_present (list[str] | None):
        has_access_token (bool | None):
        access_token_expiry (None | str):
        has_refresh_token (bool | None):
        subject (None | str):
        email (None | str):
    """

    id: str
    tenant_id: str
    scope: Schema67
    user_id: float | None
    profile_id: None | str
    last_used_at: None | str
    authorized_at: str
    type_: ServerCredentialsDtoType
    created_at: str
    updated_at: str
    user_sub: None | str
    user_email: None | str
    user_name: None | str
    profile_name: None | str
    apikeys_present: list[str] | None
    has_access_token: bool | None
    access_token_expiry: None | str
    has_refresh_token: bool | None
    subject: None | str
    email: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        scope = self.scope.value

        user_id: float | None
        user_id = self.user_id

        profile_id: None | str
        profile_id = self.profile_id

        last_used_at: None | str
        last_used_at = self.last_used_at

        authorized_at = self.authorized_at

        type_ = self.type_.value

        created_at = self.created_at

        updated_at = self.updated_at

        user_sub: None | str
        user_sub = self.user_sub

        user_email: None | str
        user_email = self.user_email

        user_name: None | str
        user_name = self.user_name

        profile_name: None | str
        profile_name = self.profile_name

        apikeys_present: list[str] | None
        if isinstance(self.apikeys_present, list):
            apikeys_present = self.apikeys_present

        else:
            apikeys_present = self.apikeys_present

        has_access_token: bool | None
        has_access_token = self.has_access_token

        access_token_expiry: None | str
        access_token_expiry = self.access_token_expiry

        has_refresh_token: bool | None
        has_refresh_token = self.has_refresh_token

        subject: None | str
        subject = self.subject

        email: None | str
        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "tenantId": tenant_id,
                "scope": scope,
                "userId": user_id,
                "profileId": profile_id,
                "lastUsedAt": last_used_at,
                "authorizedAt": authorized_at,
                "type": type_,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "userSub": user_sub,
                "userEmail": user_email,
                "userName": user_name,
                "profileName": profile_name,
                "apikeysPresent": apikeys_present,
                "hasAccessToken": has_access_token,
                "accessTokenExpiry": access_token_expiry,
                "hasRefreshToken": has_refresh_token,
                "subject": subject,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        tenant_id = d.pop("tenantId")

        scope = Schema67(d.pop("scope"))

        def _parse_user_id(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        user_id = _parse_user_id(d.pop("userId"))

        def _parse_profile_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_id = _parse_profile_id(d.pop("profileId"))

        def _parse_last_used_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_used_at = _parse_last_used_at(d.pop("lastUsedAt"))

        authorized_at = d.pop("authorizedAt")

        type_ = ServerCredentialsDtoType(d.pop("type"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_user_sub(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_sub = _parse_user_sub(d.pop("userSub"))

        def _parse_user_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_email = _parse_user_email(d.pop("userEmail"))

        def _parse_user_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_name = _parse_user_name(d.pop("userName"))

        def _parse_profile_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_name = _parse_profile_name(d.pop("profileName"))

        def _parse_apikeys_present(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                apikeys_present_type_0 = cast(list[str], data)

                return apikeys_present_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        apikeys_present = _parse_apikeys_present(d.pop("apikeysPresent"))

        def _parse_has_access_token(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        has_access_token = _parse_has_access_token(d.pop("hasAccessToken"))

        def _parse_access_token_expiry(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        access_token_expiry = _parse_access_token_expiry(d.pop("accessTokenExpiry"))

        def _parse_has_refresh_token(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        has_refresh_token = _parse_has_refresh_token(d.pop("hasRefreshToken"))

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(d.pop("subject"))

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        server_credentials_dto = cls(
            id=id,
            tenant_id=tenant_id,
            scope=scope,
            user_id=user_id,
            profile_id=profile_id,
            last_used_at=last_used_at,
            authorized_at=authorized_at,
            type_=type_,
            created_at=created_at,
            updated_at=updated_at,
            user_sub=user_sub,
            user_email=user_email,
            user_name=user_name,
            profile_name=profile_name,
            apikeys_present=apikeys_present,
            has_access_token=has_access_token,
            access_token_expiry=access_token_expiry,
            has_refresh_token=has_refresh_token,
            subject=subject,
            email=email,
        )

        return server_credentials_dto
