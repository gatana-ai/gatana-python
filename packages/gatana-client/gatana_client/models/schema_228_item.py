from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schema_228_item_action import Schema228ItemAction

T = TypeVar("T", bound="Schema228Item")


@_attrs_define
class Schema228Item:
    """
    Attributes:
        condition (str): CEL representing the condition
        action (Schema228ItemAction):
    """

    condition: str
    action: Schema228ItemAction

    def to_dict(self) -> dict[str, Any]:
        condition = self.condition

        action = self.action.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "condition": condition,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition = d.pop("condition")

        action = Schema228ItemAction(d.pop("action"))

        schema_228_item = cls(
            condition=condition,
            action=action,
        )

        return schema_228_item
