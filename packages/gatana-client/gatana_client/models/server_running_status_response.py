from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.server_pod_status import ServerPodStatus





T = TypeVar("T", bound="ServerRunningStatusResponse")



@_attrs_define
class ServerRunningStatusResponse:
    """ 
        Attributes:
            is_deployed (bool):
            is_available (bool):
            is_stabilizing (bool):
            pods (list[ServerPodStatus]):
     """

    is_deployed: bool
    is_available: bool
    is_stabilizing: bool
    pods: list[ServerPodStatus]





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_pod_status import ServerPodStatus
        is_deployed = self.is_deployed

        is_available = self.is_available

        is_stabilizing = self.is_stabilizing

        pods = []
        for pods_item_data in self.pods:
            pods_item = pods_item_data.to_dict()
            pods.append(pods_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "isDeployed": is_deployed,
            "isAvailable": is_available,
            "isStabilizing": is_stabilizing,
            "pods": pods,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_pod_status import ServerPodStatus
        d = dict(src_dict)
        is_deployed = d.pop("isDeployed")

        is_available = d.pop("isAvailable")

        is_stabilizing = d.pop("isStabilizing")

        pods = []
        _pods = d.pop("pods")
        for pods_item_data in (_pods):
            pods_item = ServerPodStatus.from_dict(pods_item_data)



            pods.append(pods_item)


        server_running_status_response = cls(
            is_deployed=is_deployed,
            is_available=is_available,
            is_stabilizing=is_stabilizing,
            pods=pods,
        )

        return server_running_status_response

