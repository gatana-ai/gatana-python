from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PersonalAccessToken")


@_attrs_define
class PersonalAccessToken:
    """
    Attributes:
        tenant_id (str):
        user_id (str):
        id (str):
        name (str):
        api_key (str):
        profile_ids (list[str]):
        created_at (str):
        last_used_at (None | str):
    """

    tenant_id: str
    user_id: str
    id: str
    name: str
    api_key: str
    profile_ids: list[str]
    created_at: str
    last_used_at: None | str

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        user_id = self.user_id

        id = self.id

        name = self.name

        api_key = self.api_key

        profile_ids = self.profile_ids

        created_at = self.created_at

        last_used_at: None | str
        last_used_at = self.last_used_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenantId": tenant_id,
                "userId": user_id,
                "id": id,
                "name": name,
                "apiKey": api_key,
                "profileIds": profile_ids,
                "createdAt": created_at,
                "lastUsedAt": last_used_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_id = d.pop("tenantId")

        user_id = d.pop("userId")

        id = d.pop("id")

        name = d.pop("name")

        api_key = d.pop("apiKey")

        profile_ids = cast(list[str], d.pop("profileIds"))

        created_at = d.pop("createdAt")

        def _parse_last_used_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_used_at = _parse_last_used_at(d.pop("lastUsedAt"))

        personal_access_token = cls(
            tenant_id=tenant_id,
            user_id=user_id,
            id=id,
            name=name,
            api_key=api_key,
            profile_ids=profile_ids,
            created_at=created_at,
            last_used_at=last_used_at,
        )

        return personal_access_token
