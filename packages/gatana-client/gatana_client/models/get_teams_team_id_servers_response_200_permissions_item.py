from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_387 import Schema387
    from ..models.schema_392 import Schema392
    from ..models.server import Server


T = TypeVar("T", bound="GetTeamsTeamIdServersResponse200PermissionsItem")


@_attrs_define
class GetTeamsTeamIdServersResponse200PermissionsItem:
    """
    Attributes:
        permission (Schema387 | Schema392):
        server (Server):
    """

    permission: Schema387 | Schema392
    server: Server

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_387 import Schema387

        permission: dict[str, Any]
        if isinstance(self.permission, Schema387):
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
        from ..models.schema_387 import Schema387
        from ..models.schema_392 import Schema392
        from ..models.server import Server

        d = dict(src_dict)

        def _parse_permission(data: object) -> Schema387 | Schema392:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_server_member_type_0 = Schema387.from_dict(data)

                return componentsschemas_server_member_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_server_member_type_1 = Schema392.from_dict(data)

            return componentsschemas_server_member_type_1

        permission = _parse_permission(d.pop("permission"))

        server = Server.from_dict(d.pop("server"))

        get_teams_team_id_servers_response_200_permissions_item = cls(
            permission=permission,
            server=server,
        )

        return get_teams_team_id_servers_response_200_permissions_item
