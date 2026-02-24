from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="ServerFile")



@_attrs_define
class ServerFile:
    """ 
        Attributes:
            tenant_id (str):
            server_id (str):
            id (str):
            filename (str):
            source_type (Literal['aws-secrets-manager'] | Literal['aws-ssm'] | Literal['gcs']):
            source_id (str):
            size (float | None):
            credential_id (None | str):
            created_at (str):
            updated_at (str):
     """

    tenant_id: str
    server_id: str
    id: str
    filename: str
    source_type: Literal['aws-secrets-manager'] | Literal['aws-ssm'] | Literal['gcs']
    source_id: str
    size: float | None
    credential_id: None | str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        server_id = self.server_id

        id = self.id

        filename = self.filename

        source_type: Literal['aws-secrets-manager'] | Literal['aws-ssm'] | Literal['gcs']
        source_type = self.source_type

        source_id = self.source_id

        size: float | None
        size = self.size

        credential_id: None | str
        credential_id = self.credential_id

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tenantId": tenant_id,
            "serverId": server_id,
            "id": id,
            "filename": filename,
            "sourceType": source_type,
            "sourceId": source_id,
            "size": size,
            "credentialId": credential_id,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_id = d.pop("tenantId")

        server_id = d.pop("serverId")

        id = d.pop("id")

        filename = d.pop("filename")

        def _parse_source_type(data: object) -> Literal['aws-secrets-manager'] | Literal['aws-ssm'] | Literal['gcs']:
            source_type_type_0 = cast(Literal['gcs'] , data)
            if source_type_type_0 != 'gcs':
                raise ValueError(f"sourceType_type_0 must match const 'gcs', got '{source_type_type_0}'")
            return source_type_type_0
            source_type_type_1 = cast(Literal['aws-ssm'] , data)
            if source_type_type_1 != 'aws-ssm':
                raise ValueError(f"sourceType_type_1 must match const 'aws-ssm', got '{source_type_type_1}'")
            return source_type_type_1
            source_type_type_2 = cast(Literal['aws-secrets-manager'] , data)
            if source_type_type_2 != 'aws-secrets-manager':
                raise ValueError(f"sourceType_type_2 must match const 'aws-secrets-manager', got '{source_type_type_2}'")
            return source_type_type_2

        source_type = _parse_source_type(d.pop("sourceType"))


        source_id = d.pop("sourceId")

        def _parse_size(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        size = _parse_size(d.pop("size"))


        def _parse_credential_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        credential_id = _parse_credential_id(d.pop("credentialId"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        server_file = cls(
            tenant_id=tenant_id,
            server_id=server_id,
            id=id,
            filename=filename,
            source_type=source_type,
            source_id=source_id,
            size=size,
            credential_id=credential_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        return server_file

