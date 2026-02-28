from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_73 import Schema73


T = TypeVar("T", bound="DeploymentLogPayloadType1")


@_attrs_define
class DeploymentLogPayloadType1:
    """
    Attributes:
        type_ (Literal['podInfo']):
        created_at (str):
        pod (str):
        init_containers (list[str]):
        containers (list[str]):
        waiting_reason (None | str):
        restart_count (float):
        has_previous_failure (bool):
        is_sandbox (bool):
        last_failure (Schema73 | Unset):
    """

    type_: Literal["podInfo"]
    created_at: str
    pod: str
    init_containers: list[str]
    containers: list[str]
    waiting_reason: None | str
    restart_count: float
    has_previous_failure: bool
    is_sandbox: bool
    last_failure: Schema73 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        created_at = self.created_at

        pod = self.pod

        init_containers = self.init_containers

        containers = self.containers

        waiting_reason: None | str
        waiting_reason = self.waiting_reason

        restart_count = self.restart_count

        has_previous_failure = self.has_previous_failure

        is_sandbox = self.is_sandbox

        last_failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_failure, Unset):
            last_failure = self.last_failure.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "createdAt": created_at,
                "pod": pod,
                "initContainers": init_containers,
                "containers": containers,
                "waitingReason": waiting_reason,
                "restartCount": restart_count,
                "hasPreviousFailure": has_previous_failure,
                "isSandbox": is_sandbox,
            }
        )
        if last_failure is not UNSET:
            field_dict["lastFailure"] = last_failure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_73 import Schema73

        d = dict(src_dict)
        type_ = cast(Literal["podInfo"], d.pop("type"))
        if type_ != "podInfo":
            raise ValueError(f"type must match const 'podInfo', got '{type_}'")

        created_at = d.pop("createdAt")

        pod = d.pop("pod")

        init_containers = cast(list[str], d.pop("initContainers"))

        containers = cast(list[str], d.pop("containers"))

        def _parse_waiting_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        waiting_reason = _parse_waiting_reason(d.pop("waitingReason"))

        restart_count = d.pop("restartCount")

        has_previous_failure = d.pop("hasPreviousFailure")

        is_sandbox = d.pop("isSandbox")

        _last_failure = d.pop("lastFailure", UNSET)
        last_failure: Schema73 | Unset
        if isinstance(_last_failure, Unset):
            last_failure = UNSET
        else:
            last_failure = Schema73.from_dict(_last_failure)

        deployment_log_payload_type_1 = cls(
            type_=type_,
            created_at=created_at,
            pod=pod,
            init_containers=init_containers,
            containers=containers,
            waiting_reason=waiting_reason,
            restart_count=restart_count,
            has_previous_failure=has_previous_failure,
            is_sandbox=is_sandbox,
            last_failure=last_failure,
        )

        return deployment_log_payload_type_1
