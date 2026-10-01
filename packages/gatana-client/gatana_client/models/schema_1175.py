from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.schema_1119 import Schema1119

if TYPE_CHECKING:
    from ..models.schema_1170 import Schema1170
    from ..models.schema_1173 import Schema1173


T = TypeVar("T", bound="Schema1175")


@_attrs_define
class Schema1175:
    """
    Attributes:
        collection_id (str):
        collection_name (str):
        visibility (Schema1119):
        users (list[Schema1170]): User accounts with access, oldest share first
        teams (list[Schema1173]): Teams with access, oldest share first; every member of a team has it
    """

    collection_id: str
    collection_name: str
    visibility: Schema1119
    users: list[Schema1170]
    teams: list[Schema1173]

    def to_dict(self) -> dict[str, Any]:
        collection_id = self.collection_id

        collection_name = self.collection_name

        visibility = self.visibility.value

        users = []
        for componentsschemas_schema1169_item_data in self.users:
            componentsschemas_schema1169_item = componentsschemas_schema1169_item_data.to_dict()
            users.append(componentsschemas_schema1169_item)

        teams = []
        for componentsschemas_schema1172_item_data in self.teams:
            componentsschemas_schema1172_item = componentsschemas_schema1172_item_data.to_dict()
            teams.append(componentsschemas_schema1172_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "collectionId": collection_id,
                "collectionName": collection_name,
                "visibility": visibility,
                "users": users,
                "teams": teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_1170 import Schema1170
        from ..models.schema_1173 import Schema1173

        d = dict(src_dict)
        collection_id = d.pop("collectionId")

        collection_name = d.pop("collectionName")

        visibility = Schema1119(d.pop("visibility"))

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

        schema_1175 = cls(
            collection_id=collection_id,
            collection_name=collection_name,
            visibility=visibility,
            users=users,
            teams=teams,
        )

        return schema_1175
