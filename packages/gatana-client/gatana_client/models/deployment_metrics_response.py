from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.schema_795 import Schema795
    from ..models.schema_800 import Schema800
    from ..models.schema_801 import Schema801
    from ..models.schema_807 import Schema807


T = TypeVar("T", bound="DeploymentMetricsResponse")


@_attrs_define
class DeploymentMetricsResponse:
    """
    Attributes:
        cpu (Schema795):
        memory (Schema800):
        resource_limits (Schema801):
        storage (None | Schema807): Usage of the server's persistent volume, or null when it keeps no state or reports
            no usage
    """

    cpu: Schema795
    memory: Schema800
    resource_limits: Schema801
    storage: None | Schema807

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_807 import Schema807

        cpu = self.cpu.to_dict()

        memory = self.memory.to_dict()

        resource_limits = self.resource_limits.to_dict()

        storage: dict[str, Any] | None
        if isinstance(self.storage, Schema807):
            storage = self.storage.to_dict()
        else:
            storage = self.storage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cpu": cpu,
                "memory": memory,
                "resourceLimits": resource_limits,
                "storage": storage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_795 import Schema795
        from ..models.schema_800 import Schema800
        from ..models.schema_801 import Schema801
        from ..models.schema_807 import Schema807

        d = dict(src_dict)
        cpu = Schema795.from_dict(d.pop("cpu"))

        memory = Schema800.from_dict(d.pop("memory"))

        resource_limits = Schema801.from_dict(d.pop("resourceLimits"))

        def _parse_storage(data: object) -> None | Schema807:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema806_type_0 = Schema807.from_dict(data)

                return componentsschemas_schema806_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Schema807, data)

        storage = _parse_storage(d.pop("storage"))

        deployment_metrics_response = cls(
            cpu=cpu,
            memory=memory,
            resource_limits=resource_limits,
            storage=storage,
        )

        return deployment_metrics_response
