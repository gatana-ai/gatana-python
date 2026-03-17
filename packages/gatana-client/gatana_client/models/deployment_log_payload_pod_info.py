from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schema_345 import Schema345
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_335 import Schema335
    from ..models.schema_354 import Schema354


T = TypeVar("T", bound="DeploymentLogPayloadPodInfo")


@_attrs_define
class DeploymentLogPayloadPodInfo:
    """
    Attributes:
        type_ (Literal['podInfo']):
        status (Schema345):
        created_at (str):
        pod (str):
        init_containers (list[str]):
        containers (list[str]):
        waiting_reason (None | str):
        restart_count (float):
        has_previous_failure (bool):
        last_fail_condition (None | Schema335):
        is_sandbox (bool):
        last_failure (Schema354 | Unset):
    """

    type_: Literal["podInfo"]
    status: Schema345
    created_at: str
    pod: str
    init_containers: list[str]
    containers: list[str]
    waiting_reason: None | str
    restart_count: float
    has_previous_failure: bool
    last_fail_condition: None | Schema335
    is_sandbox: bool
    last_failure: Schema354 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_335 import Schema335

        type_ = self.type_

        status = self.status.value

        created_at = self.created_at

        pod = self.pod

        init_containers = self.init_containers

        containers = self.containers

        waiting_reason: None | str
        waiting_reason = self.waiting_reason

        restart_count = self.restart_count

        has_previous_failure = self.has_previous_failure

        last_fail_condition: dict[str, Any] | None
        if isinstance(self.last_fail_condition, Schema335):
            last_fail_condition = self.last_fail_condition.to_dict()
        else:
            last_fail_condition = self.last_fail_condition

        is_sandbox = self.is_sandbox

        last_failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_failure, Unset):
            last_failure = self.last_failure.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "status": status,
                "createdAt": created_at,
                "pod": pod,
                "initContainers": init_containers,
                "containers": containers,
                "waitingReason": waiting_reason,
                "restartCount": restart_count,
                "hasPreviousFailure": has_previous_failure,
                "lastFailCondition": last_fail_condition,
                "isSandbox": is_sandbox,
            }
        )
        if last_failure is not UNSET:
            field_dict["lastFailure"] = last_failure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_335 import Schema335
        from ..models.schema_354 import Schema354

        d = dict(src_dict)
        type_ = cast(Literal["podInfo"], d.pop("type"))
        if type_ != "podInfo":
            raise ValueError(f"type must match const 'podInfo', got '{type_}'")

        status = Schema345(d.pop("status"))

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

        def _parse_last_fail_condition(data: object) -> None | Schema335:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_schema353_type_0 = Schema335.from_dict(data)

                return componentsschemas_schema353_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Schema335, data)

        last_fail_condition = _parse_last_fail_condition(d.pop("lastFailCondition"))

        is_sandbox = d.pop("isSandbox")

        _last_failure = d.pop("lastFailure", UNSET)
        last_failure: Schema354 | Unset
        if isinstance(_last_failure, Unset):
            last_failure = UNSET
        else:
            last_failure = Schema354.from_dict(_last_failure)

        deployment_log_payload_pod_info = cls(
            type_=type_,
            status=status,
            created_at=created_at,
            pod=pod,
            init_containers=init_containers,
            containers=containers,
            waiting_reason=waiting_reason,
            restart_count=restart_count,
            has_previous_failure=has_previous_failure,
            last_fail_condition=last_fail_condition,
            is_sandbox=is_sandbox,
            last_failure=last_failure,
        )

        return deployment_log_payload_pod_info
