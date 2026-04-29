from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_256 import Schema256
    from ..models.schema_257_type_0 import Schema257Type0
    from ..models.schema_258_type_0 import Schema258Type0


T = TypeVar("T", bound="ServerToolDto")


@_attrs_define
class ServerToolDto:
    """
    Attributes:
        tenant_id (str):
        tool_name (str):
        description (str):
        schema (Schema256):
        output_schema (None | Schema257Type0):
        annotations (None | Schema258Type0):
        is_enabled (bool):
        server_slug (str):
        universal_name (str):
    """

    tenant_id: str
    tool_name: str
    description: str
    schema: Schema256
    output_schema: None | Schema257Type0
    annotations: None | Schema258Type0
    is_enabled: bool
    server_slug: str
    universal_name: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_257_type_0 import Schema257Type0
        from ..models.schema_258_type_0 import Schema258Type0

        tenant_id = self.tenant_id

        tool_name = self.tool_name

        description = self.description

        schema = self.schema.to_dict()

        output_schema: dict[str, Any] | None
        if isinstance(self.output_schema, Schema257Type0):
            output_schema = self.output_schema.to_dict()
        else:
            output_schema = self.output_schema

        annotations: dict[str, Any] | None
        if isinstance(self.annotations, Schema258Type0):
            annotations = self.annotations.to_dict()
        else:
            annotations = self.annotations

        is_enabled = self.is_enabled

        server_slug = self.server_slug

        universal_name = self.universal_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tenantId": tenant_id,
                "toolName": tool_name,
                "description": description,
                "schema": schema,
                "outputSchema": output_schema,
                "annotations": annotations,
                "isEnabled": is_enabled,
                "serverSlug": server_slug,
                "universalName": universal_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_256 import Schema256
        from ..models.schema_257_type_0 import Schema257Type0
        from ..models.schema_258_type_0 import Schema258Type0

        d = dict(src_dict)
        tenant_id = d.pop("tenantId")

        tool_name = d.pop("toolName")

        description = d.pop("description")

        schema = Schema256.from_dict(d.pop("schema"))

        def _parse_output_schema(data: object) -> None | Schema257Type0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema257_type_0 = Schema257Type0.from_dict(data)

                return componentsschemas_schema257_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Schema257Type0, data)

        output_schema = _parse_output_schema(d.pop("outputSchema"))

        def _parse_annotations(data: object) -> None | Schema258Type0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema258_type_0 = Schema258Type0.from_dict(data)

                return componentsschemas_schema258_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Schema258Type0, data)

        annotations = _parse_annotations(d.pop("annotations"))

        is_enabled = d.pop("isEnabled")

        server_slug = d.pop("serverSlug")

        universal_name = d.pop("universalName")

        server_tool_dto = cls(
            tenant_id=tenant_id,
            tool_name=tool_name,
            description=description,
            schema=schema,
            output_schema=output_schema,
            annotations=annotations,
            is_enabled=is_enabled,
            server_slug=server_slug,
            universal_name=universal_name,
        )

        return server_tool_dto
