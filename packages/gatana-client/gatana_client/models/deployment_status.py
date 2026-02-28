from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_73 import Schema73


T = TypeVar("T", bound="DeploymentStatus")


@_attrs_define
class DeploymentStatus:
    """
    Attributes:
        name (str):
        ready (bool):
        crash (bool):
        restart_count (float):
        has_previous_failure (bool):
        phase (str | Unset):
        reason (str | Unset):
        created_at (str | Unset):
        last_failure (Schema73 | Unset):
        waiting_reason (str | Unset):
    """

    name: str
    ready: bool
    crash: bool
    restart_count: float
    has_previous_failure: bool
    phase: str | Unset = UNSET
    reason: str | Unset = UNSET
    created_at: str | Unset = UNSET
    last_failure: Schema73 | Unset = UNSET
    waiting_reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ready = self.ready

        crash = self.crash

        restart_count = self.restart_count

        has_previous_failure = self.has_previous_failure

        phase = self.phase

        reason = self.reason

        created_at = self.created_at

        last_failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_failure, Unset):
            last_failure = self.last_failure.to_dict()

        waiting_reason = self.waiting_reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "ready": ready,
                "crash": crash,
                "restartCount": restart_count,
                "hasPreviousFailure": has_previous_failure,
            }
        )
        if phase is not UNSET:
            field_dict["phase"] = phase
        if reason is not UNSET:
            field_dict["reason"] = reason
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_failure is not UNSET:
            field_dict["lastFailure"] = last_failure
        if waiting_reason is not UNSET:
            field_dict["waitingReason"] = waiting_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_73 import Schema73

        d = dict(src_dict)
        name = d.pop("name")

        ready = d.pop("ready")

        crash = d.pop("crash")

        restart_count = d.pop("restartCount")

        has_previous_failure = d.pop("hasPreviousFailure")

        phase = d.pop("phase", UNSET)

        reason = d.pop("reason", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _last_failure = d.pop("lastFailure", UNSET)
        last_failure: Schema73 | Unset
        if isinstance(_last_failure, Unset):
            last_failure = UNSET
        else:
            last_failure = Schema73.from_dict(_last_failure)

        waiting_reason = d.pop("waitingReason", UNSET)

        deployment_status = cls(
            name=name,
            ready=ready,
            crash=crash,
            restart_count=restart_count,
            has_previous_failure=has_previous_failure,
            phase=phase,
            reason=reason,
            created_at=created_at,
            last_failure=last_failure,
            waiting_reason=waiting_reason,
        )

        return deployment_status
