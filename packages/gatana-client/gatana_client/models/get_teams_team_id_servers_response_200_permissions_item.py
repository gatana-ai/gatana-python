from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_415 import Schema415
    from ..models.schema_420 import Schema420
    from ..models.server import Server


T = TypeVar("T", bound="GetTeamsTeamIdServersResponse200PermissionsItem")


@_attrs_define
class GetTeamsTeamIdServersResponse200PermissionsItem:
    """
    Attributes:
        permission (Schema415 | Schema420):
        server (Server):
    """

    permission: Schema415 | Schema420
    server: Server

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_415 import Schema415

        permission: dict[str, Any]
        if isinstance(self.permission, Schema415):
            permission = self.permission.to_dict()
        else:
            permission = self.permission.to_dict()

        server = self.server.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "permission": permission,
                "server": server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_415 import Schema415
        from ..models.schema_420 import Schema420
        from ..models.server import Server

        d = dict(src_dict)

        def _parse_permission(data: object) -> Schema415 | Schema420:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_server_member_type_0 = Schema415.from_dict(data)

                return componentsschemas_server_member_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_server_member_type_1 = Schema420.from_dict(data)

            return componentsschemas_server_member_type_1

        permission = _parse_permission(d.pop("permission"))

        server = Server.from_dict(d.pop("server"))

        get_teams_team_id_servers_response_200_permissions_item = cls(
            permission=permission,
            server=server,
        )

        return get_teams_team_id_servers_response_200_permissions_item
