from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_420 import Schema420
    from ..models.schema_425 import Schema425


T = TypeVar("T", bound="GetTeamsTeamIdServersResponse200PermissionsItem")


@_attrs_define
class GetTeamsTeamIdServersResponse200PermissionsItem:
    """
    Attributes:
        permission (Schema420 | Schema425):
        server_slug (str):
    """

    permission: Schema420 | Schema425
    server_slug: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_420 import Schema420

        permission: dict[str, Any]
        if isinstance(self.permission, Schema420):
            permission = self.permission.to_dict()
        else:
            permission = self.permission.to_dict()

        server_slug = self.server_slug

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "permission": permission,
                "serverSlug": server_slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_420 import Schema420
        from ..models.schema_425 import Schema425

        d = dict(src_dict)

        def _parse_permission(data: object) -> Schema420 | Schema425:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_server_member_type_0 = Schema420.from_dict(data)

                return componentsschemas_server_member_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_server_member_type_1 = Schema425.from_dict(data)

            return componentsschemas_server_member_type_1

        permission = _parse_permission(d.pop("permission"))

        server_slug = d.pop("serverSlug")

        get_teams_team_id_servers_response_200_permissions_item = cls(
            permission=permission,
            server_slug=server_slug,
        )

        return get_teams_team_id_servers_response_200_permissions_item
