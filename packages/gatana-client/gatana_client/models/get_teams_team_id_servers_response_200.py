from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_teams_team_id_servers_response_200_permissions_item import GetTeamsTeamIdServersResponse200PermissionsItem





T = TypeVar("T", bound="GetTeamsTeamIdServersResponse200")



@_attrs_define
class GetTeamsTeamIdServersResponse200:
    """ 
        Attributes:
            permissions (list[GetTeamsTeamIdServersResponse200PermissionsItem]):
     """

    permissions: list[GetTeamsTeamIdServersResponse200PermissionsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_teams_team_id_servers_response_200_permissions_item import GetTeamsTeamIdServersResponse200PermissionsItem
        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "permissions": permissions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_teams_team_id_servers_response_200_permissions_item import GetTeamsTeamIdServersResponse200PermissionsItem
        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = GetTeamsTeamIdServersResponse200PermissionsItem.from_dict(permissions_item_data)



            permissions.append(permissions_item)


        get_teams_team_id_servers_response_200 = cls(
            permissions=permissions,
        )

        return get_teams_team_id_servers_response_200

