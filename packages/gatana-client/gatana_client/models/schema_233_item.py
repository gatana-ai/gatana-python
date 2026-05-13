from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schema_233_item_action import Schema233ItemAction

T = TypeVar("T", bound="Schema233Item")


@_attrs_define
class Schema233Item:
    """
    Attributes:
        condition (str): CEL representing the condition
        action (Schema233ItemAction):
    """

    condition: str
    action: Schema233ItemAction

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

        action = Schema233ItemAction(d.pop("action"))

        schema_233_item = cls(
            condition=condition,
            action=action,
        )

        return schema_233_item
