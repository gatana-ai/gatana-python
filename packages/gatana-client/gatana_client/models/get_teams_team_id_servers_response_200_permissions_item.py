from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.server import Server
  from ..models.server_member_type_0 import ServerMemberType0
  from ..models.server_member_type_1 import ServerMemberType1





T = TypeVar("T", bound="GetTeamsTeamIdServersResponse200PermissionsItem")



@_attrs_define
class GetTeamsTeamIdServersResponse200PermissionsItem:
    """ 
        Attributes:
            permission (ServerMemberType0 | ServerMemberType1):
            server (Server):
     """

    permission: ServerMemberType0 | ServerMemberType1
    server: Server





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_member_type_1 import ServerMemberType1
        from ..models.server import Server
        from ..models.server_member_type_0 import ServerMemberType0
        permission: dict[str, Any]
        if isinstance(self.permission, ServerMemberType0):
            permission = self.permission.to_dict()
        else:
            permission = self.permission.to_dict()


        server = self.server.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "permission": permission,
            "server": server,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server import Server
        from ..models.server_member_type_0 import ServerMemberType0
        from ..models.server_member_type_1 import ServerMemberType1
        d = dict(src_dict)
        def _parse_permission(data: object) -> ServerMemberType0 | ServerMemberType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_server_member_type_0 = ServerMemberType0.from_dict(data)



                return componentsschemas_server_member_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_server_member_type_1 = ServerMemberType1.from_dict(data)



            return componentsschemas_server_member_type_1

        permission = _parse_permission(d.pop("permission"))


        server = Server.from_dict(d.pop("server"))




        get_teams_team_id_servers_response_200_permissions_item = cls(
            permission=permission,
            server=server,
        )

        return get_teams_team_id_servers_response_200_permissions_item

