from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Schema41")


@_attrs_define
class Schema41:
    """
    Attributes:
        page (float):
        limit (float):
        total (float):
        total_pages (float):
        has_next (bool):
        has_prev (bool):
    """

    page: float
    limit: float
    total: float
    total_pages: float
    has_next: bool
    has_prev: bool

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        limit = self.limit

        total = self.total

        total_pages = self.total_pages

        has_next = self.has_next

        has_prev = self.has_prev

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "page": page,
                "limit": limit,
                "total": total,
                "totalPages": total_pages,
                "hasNext": has_next,
                "hasPrev": has_prev,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page")

        limit = d.pop("limit")

        total = d.pop("total")

        total_pages = d.pop("totalPages")

        has_next = d.pop("hasNext")

        has_prev = d.pop("hasPrev")

        schema_41 = cls(
            page=page,
            limit=limit,
            total=total,
            total_pages=total_pages,
            has_next=has_next,
            has_prev=has_prev,
        )

        return schema_41
