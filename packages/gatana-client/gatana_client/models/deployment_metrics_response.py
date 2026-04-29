from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.metrics_time_series import MetricsTimeSeries
    from ..models.resource_limits import ResourceLimits


T = TypeVar("T", bound="DeploymentMetricsResponse")


@_attrs_define
class DeploymentMetricsResponse:
    """
    Attributes:
        cpu (MetricsTimeSeries):
        memory (MetricsTimeSeries):
        resource_limits (ResourceLimits):
    """

    cpu: MetricsTimeSeries
    memory: MetricsTimeSeries
    resource_limits: ResourceLimits

    def to_dict(self) -> dict[str, Any]:
        cpu = self.cpu.to_dict()

        memory = self.memory.to_dict()

        resource_limits = self.resource_limits.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cpu": cpu,
                "memory": memory,
                "resourceLimits": resource_limits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_time_series import MetricsTimeSeries
        from ..models.resource_limits import ResourceLimits

        d = dict(src_dict)
        cpu = MetricsTimeSeries.from_dict(d.pop("cpu"))

        memory = MetricsTimeSeries.from_dict(d.pop("memory"))

        resource_limits = ResourceLimits.from_dict(d.pop("resourceLimits"))

        deployment_metrics_response = cls(
            cpu=cpu,
            memory=memory,
            resource_limits=resource_limits,
        )

        return deployment_metrics_response
