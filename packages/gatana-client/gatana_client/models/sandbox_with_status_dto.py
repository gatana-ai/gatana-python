from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sandbox_with_status_dto_status import SandboxWithStatusDtoStatus
    from ..models.user_small_dto import UserSmallDto


T = TypeVar("T", bound="SandboxWithStatusDto")


@_attrs_define
class SandboxWithStatusDto:
    """
    Attributes:
        id (str):
        tenant_id (str):
        kubernetes_deployment_name (str):
        last_activity_at (str):
        created_at (str):
        updated_at (str):
        user (UserSmallDto):
        status (SandboxWithStatusDtoStatus):
    """

    id: str
    tenant_id: str
    kubernetes_deployment_name: str
    last_activity_at: str
    created_at: str
    updated_at: str
    user: UserSmallDto
    status: SandboxWithStatusDtoStatus

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        kubernetes_deployment_name = self.kubernetes_deployment_name

        last_activity_at = self.last_activity_at

        created_at = self.created_at

        updated_at = self.updated_at

        user = self.user.to_dict()

        status = self.status.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "tenantId": tenant_id,
                "kubernetesDeploymentName": kubernetes_deployment_name,
                "lastActivityAt": last_activity_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "user": user,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_with_status_dto_status import SandboxWithStatusDtoStatus
        from ..models.user_small_dto import UserSmallDto

        d = dict(src_dict)
        id = d.pop("id")

        tenant_id = d.pop("tenantId")

        kubernetes_deployment_name = d.pop("kubernetesDeploymentName")

        last_activity_at = d.pop("lastActivityAt")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        user = UserSmallDto.from_dict(d.pop("user"))

        status = SandboxWithStatusDtoStatus.from_dict(d.pop("status"))

        sandbox_with_status_dto = cls(
            id=id,
            tenant_id=tenant_id,
            kubernetes_deployment_name=kubernetes_deployment_name,
            last_activity_at=last_activity_at,
            created_at=created_at,
            updated_at=updated_at,
            user=user,
            status=status,
        )

        return sandbox_with_status_dto
