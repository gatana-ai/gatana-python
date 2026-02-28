from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schema_72 import Schema72

if TYPE_CHECKING:
    from ..models.server_authorization_output import ServerAuthorizationOutput
    from ..models.server_credentials_dto import ServerCredentialsDto


T = TypeVar("T", bound="ProfileDetailsDtoServersItem")


@_attrs_define
class ProfileDetailsDtoServersItem:
    """
    Attributes:
        name (str):
        slug (str):
        authorization (ServerAuthorizationOutput):
        credentials_num_keys (float | None):
        credential_scope (Schema72):
        credentials (None | ServerCredentialsDto):
    """

    name: str
    slug: str
    authorization: ServerAuthorizationOutput
    credentials_num_keys: float | None
    credential_scope: Schema72
    credentials: None | ServerCredentialsDto

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_credentials_dto import ServerCredentialsDto

        name = self.name

        slug = self.slug

        authorization = self.authorization.to_dict()

        credentials_num_keys: float | None
        credentials_num_keys = self.credentials_num_keys

        credential_scope = self.credential_scope.value

        credentials: dict[str, Any] | None
        if isinstance(self.credentials, ServerCredentialsDto):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "authorization": authorization,
                "credentialsNumKeys": credentials_num_keys,
                "credentialScope": credential_scope,
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_authorization_output import ServerAuthorizationOutput
        from ..models.server_credentials_dto import ServerCredentialsDto

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        authorization = ServerAuthorizationOutput.from_dict(d.pop("authorization"))

        def _parse_credentials_num_keys(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        credentials_num_keys = _parse_credentials_num_keys(d.pop("credentialsNumKeys"))

        credential_scope = Schema72(d.pop("credentialScope"))

        def _parse_credentials(data: object) -> None | ServerCredentialsDto:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = ServerCredentialsDto.from_dict(data)

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerCredentialsDto, data)

        credentials = _parse_credentials(d.pop("credentials"))

        profile_details_dto_servers_item = cls(
            name=name,
            slug=slug,
            authorization=authorization,
            credentials_num_keys=credentials_num_keys,
            credential_scope=credential_scope,
            credentials=credentials,
        )

        return profile_details_dto_servers_item
