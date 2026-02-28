from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_status import DeploymentStatus


T = TypeVar("T", bound="DeploymentStatusResponse")


@_attrs_define
class DeploymentStatusResponse:
    """
    Attributes:
        is_deployed (bool):
        is_available (bool):
        is_stabilizing (bool):
        deployments (list[DeploymentStatus]):
        current_replica_set (str | Unset):
    """

    is_deployed: bool
    is_available: bool
    is_stabilizing: bool
    deployments: list[DeploymentStatus]
    current_replica_set: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_deployed = self.is_deployed

        is_available = self.is_available

        is_stabilizing = self.is_stabilizing

        deployments = []
        for deployments_item_data in self.deployments:
            deployments_item = deployments_item_data.to_dict()
            deployments.append(deployments_item)

        current_replica_set = self.current_replica_set

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isDeployed": is_deployed,
                "isAvailable": is_available,
                "isStabilizing": is_stabilizing,
                "deployments": deployments,
            }
        )
        if current_replica_set is not UNSET:
            field_dict["currentReplicaSet"] = current_replica_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_status import DeploymentStatus

        d = dict(src_dict)
        is_deployed = d.pop("isDeployed")

        is_available = d.pop("isAvailable")

        is_stabilizing = d.pop("isStabilizing")

        deployments = []
        _deployments = d.pop("deployments")
        for deployments_item_data in _deployments:
            deployments_item = DeploymentStatus.from_dict(deployments_item_data)

            deployments.append(deployments_item)

        current_replica_set = d.pop("currentReplicaSet", UNSET)

        deployment_status_response = cls(
            is_deployed=is_deployed,
            is_available=is_available,
            is_stabilizing=is_stabilizing,
            deployments=deployments,
            current_replica_set=current_replica_set,
        )

        return deployment_status_response
