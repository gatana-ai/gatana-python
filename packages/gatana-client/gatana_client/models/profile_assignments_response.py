from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_1015 import Schema1015
    from ..models.schema_1020 import Schema1020


T = TypeVar("T", bound="ProfileAssignmentsResponse")


@_attrs_define
class ProfileAssignmentsResponse:
    """
    Attributes:
        accounts (list[Schema1015]): Users directly assigned to the profile
        teams (list[Schema1020]): Teams assigned to the profile
    """

    accounts: list[Schema1015]
    teams: list[Schema1020]

    def to_dict(self) -> dict[str, Any]:
        accounts = []
        for componentsschemas_schema1014_item_data in self.accounts:
            componentsschemas_schema1014_item = componentsschemas_schema1014_item_data.to_dict()
            accounts.append(componentsschemas_schema1014_item)

        teams = []
        for componentsschemas_schema1019_item_data in self.teams:
            componentsschemas_schema1019_item = componentsschemas_schema1019_item_data.to_dict()
            teams.append(componentsschemas_schema1019_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accounts": accounts,
                "teams": teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_1015 import Schema1015
        from ..models.schema_1020 import Schema1020

        d = dict(src_dict)
        accounts = []
        _accounts = d.pop("accounts")
        for componentsschemas_schema1014_item_data in _accounts:
            componentsschemas_schema1014_item = Schema1015.from_dict(componentsschemas_schema1014_item_data)

            accounts.append(componentsschemas_schema1014_item)

        teams = []
        _teams = d.pop("teams")
        for componentsschemas_schema1019_item_data in _teams:
            componentsschemas_schema1019_item = Schema1020.from_dict(componentsschemas_schema1019_item_data)

            teams.append(componentsschemas_schema1019_item)

        profile_assignments_response = cls(
            accounts=accounts,
            teams=teams,
        )

        return profile_assignments_response
