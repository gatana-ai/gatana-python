from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schema_36 import Schema36
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerAuthorization")


@_attrs_define
class ServerAuthorization:
    """
    Attributes:
        method (Schema36):
        credentials_scope (Literal['server'] | Literal['user']):
        apikeys (list[str] | Unset):
    """

    method: Schema36
    credentials_scope: Literal["server"] | Literal["user"]
    apikeys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        credentials_scope: Literal["server"] | Literal["user"]
        credentials_scope = self.credentials_scope

        apikeys: list[str] | Unset = UNSET
        if not isinstance(self.apikeys, Unset):
            apikeys = self.apikeys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "credentialsScope": credentials_scope,
            }
        )
        if apikeys is not UNSET:
            field_dict["apikeys"] = apikeys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = Schema36(d.pop("method"))

        def _parse_credentials_scope(data: object) -> Literal["server"] | Literal["user"]:
            componentsschemas_schema37_type_0 = cast(Literal["server"], data)
            if componentsschemas_schema37_type_0 != "server":
                raise ValueError(
                    f"/components/schemas/__schema37_type_0 must match const 'server', got '{componentsschemas_schema37_type_0}'"
                )
            return componentsschemas_schema37_type_0
            componentsschemas_schema37_type_1 = cast(Literal["user"], data)
            if componentsschemas_schema37_type_1 != "user":
                raise ValueError(
                    f"/components/schemas/__schema37_type_1 must match const 'user', got '{componentsschemas_schema37_type_1}'"
                )
            return componentsschemas_schema37_type_1

        credentials_scope = _parse_credentials_scope(d.pop("credentialsScope"))

        apikeys = cast(list[str], d.pop("apikeys", UNSET))

        server_authorization = cls(
            method=method,
            credentials_scope=credentials_scope,
            apikeys=apikeys,
        )

        server_authorization.additional_properties = d
        return server_authorization

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
