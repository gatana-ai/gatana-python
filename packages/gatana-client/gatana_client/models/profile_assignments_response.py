from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_487_item import Schema487Item


T = TypeVar("T", bound="ProfileAssignmentsResponse")


@_attrs_define
class ProfileAssignmentsResponse:
    """
    Attributes:
        accounts (list[Schema487Item]):
    """

    accounts: list[Schema487Item]

    def to_dict(self) -> dict[str, Any]:
        accounts = []
        for componentsschemas_schema487_item_data in self.accounts:
            componentsschemas_schema487_item = componentsschemas_schema487_item_data.to_dict()
            accounts.append(componentsschemas_schema487_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accounts": accounts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_487_item import Schema487Item

        d = dict(src_dict)
        accounts = []
        _accounts = d.pop("accounts")
        for componentsschemas_schema487_item_data in _accounts:
            componentsschemas_schema487_item = Schema487Item.from_dict(componentsschemas_schema487_item_data)

            accounts.append(componentsschemas_schema487_item)

        profile_assignments_response = cls(
            accounts=accounts,
        )

        return profile_assignments_response
