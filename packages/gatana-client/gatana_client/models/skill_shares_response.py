from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_1170 import Schema1170
    from ..models.schema_1173 import Schema1173
    from ..models.schema_1175 import Schema1175


T = TypeVar("T", bound="SkillSharesResponse")


@_attrs_define
class SkillSharesResponse:
    """
    Attributes:
        users (list[Schema1170]): User accounts with access, oldest share first
        teams (list[Schema1173]): Teams with access, oldest share first; every member of a team has it
        inherited (None | Schema1175): The collection's shares, which apply to this skill as well; null at root
    """

    users: list[Schema1170]
    teams: list[Schema1173]
    inherited: None | Schema1175

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_1175 import Schema1175

        users = []
        for componentsschemas_schema1169_item_data in self.users:
            componentsschemas_schema1169_item = componentsschemas_schema1169_item_data.to_dict()
            users.append(componentsschemas_schema1169_item)

        teams = []
        for componentsschemas_schema1172_item_data in self.teams:
            componentsschemas_schema1172_item = componentsschemas_schema1172_item_data.to_dict()
            teams.append(componentsschemas_schema1172_item)

        inherited: dict[str, Any] | None
        if isinstance(self.inherited, Schema1175):
            inherited = self.inherited.to_dict()
        else:
            inherited = self.inherited

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "users": users,
                "teams": teams,
                "inherited": inherited,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_1170 import Schema1170
        from ..models.schema_1173 import Schema1173
        from ..models.schema_1175 import Schema1175

        d = dict(src_dict)
        users = []
        _users = d.pop("users")
        for componentsschemas_schema1169_item_data in _users:
            componentsschemas_schema1169_item = Schema1170.from_dict(componentsschemas_schema1169_item_data)

            users.append(componentsschemas_schema1169_item)

        teams = []
        _teams = d.pop("teams")
        for componentsschemas_schema1172_item_data in _teams:
            componentsschemas_schema1172_item = Schema1173.from_dict(componentsschemas_schema1172_item_data)

            teams.append(componentsschemas_schema1172_item)

        def _parse_inherited(data: object) -> None | Schema1175:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema1174_type_0 = Schema1175.from_dict(data)

                return componentsschemas_schema1174_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Schema1175, data)

        inherited = _parse_inherited(d.pop("inherited"))

        skill_shares_response = cls(
            users=users,
            teams=teams,
            inherited=inherited,
        )

        return skill_shares_response
