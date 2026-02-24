from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.server_authorization_output_method import ServerAuthorizationOutputMethod
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="ServerAuthorizationOutput")



@_attrs_define
class ServerAuthorizationOutput:
    """ 
        Attributes:
            method (ServerAuthorizationOutputMethod):
            credentials_scope (Literal['server'] | Literal['user']):
            apikeys (list[str] | Unset):
     """

    method: ServerAuthorizationOutputMethod
    credentials_scope: Literal['server'] | Literal['user']
    apikeys: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        credentials_scope: Literal['server'] | Literal['user']
        credentials_scope = self.credentials_scope

        apikeys: list[str] | Unset = UNSET
        if not isinstance(self.apikeys, Unset):
            apikeys = self.apikeys




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "method": method,
            "credentialsScope": credentials_scope,
        })
        if apikeys is not UNSET:
            field_dict["apikeys"] = apikeys

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = ServerAuthorizationOutputMethod(d.pop("method"))




        def _parse_credentials_scope(data: object) -> Literal['server'] | Literal['user']:
            credentials_scope_type_0 = cast(Literal['server'] , data)
            if credentials_scope_type_0 != 'server':
                raise ValueError(f"credentialsScope_type_0 must match const 'server', got '{credentials_scope_type_0}'")
            return credentials_scope_type_0
            credentials_scope_type_1 = cast(Literal['user'] , data)
            if credentials_scope_type_1 != 'user':
                raise ValueError(f"credentialsScope_type_1 must match const 'user', got '{credentials_scope_type_1}'")
            return credentials_scope_type_1

        credentials_scope = _parse_credentials_scope(d.pop("credentialsScope"))


        apikeys = cast(list[str], d.pop("apikeys", UNSET))


        server_authorization_output = cls(
            method=method,
            credentials_scope=credentials_scope,
            apikeys=apikeys,
        )

        return server_authorization_output

