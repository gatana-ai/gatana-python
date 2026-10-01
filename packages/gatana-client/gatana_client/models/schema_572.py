from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schema_572_action import Schema572Action

T = TypeVar("T", bound="Schema572")


@_attrs_define
class Schema572:
    """
    Attributes:
        condition (str): CEL representing the condition
        action (Schema572Action): Action to take when the condition matches
    """

    condition: str
    action: Schema572Action

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

        action = Schema572Action(d.pop("action"))

        schema_572 = cls(
            condition=condition,
            action=action,
        )

        return schema_572
