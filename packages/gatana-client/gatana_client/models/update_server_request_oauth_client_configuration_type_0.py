from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_server_request_oauth_client_configuration_type_0_grant_type import UpdateServerRequestOauthClientConfigurationType0GrantType
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="UpdateServerRequestOauthClientConfigurationType0")



@_attrs_define
class UpdateServerRequestOauthClientConfigurationType0:
    """ 
        Attributes:
            client_id (str | Unset):  Default: ''.
            client_secret (str | Unset):  Default: ''.
            grant_type (UpdateServerRequestOauthClientConfigurationType0GrantType | Unset):
            client_auth_method (Literal['client_secret_basic'] | Literal['client_secret_post'] | Literal['none'] | str |
                Unset):
            scopes (str | Unset):  Default: ''.
     """

    client_id: str | Unset = ''
    client_secret: str | Unset = ''
    grant_type: UpdateServerRequestOauthClientConfigurationType0GrantType | Unset = UNSET
    client_auth_method: Literal['client_secret_basic'] | Literal['client_secret_post'] | Literal['none'] | str | Unset = UNSET
    scopes: str | Unset = ''
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        grant_type: str | Unset = UNSET
        if not isinstance(self.grant_type, Unset):
            grant_type = self.grant_type.value


        client_auth_method: Literal['client_secret_basic'] | Literal['client_secret_post'] | Literal['none'] | str | Unset
        if isinstance(self.client_auth_method, Unset):
            client_auth_method = UNSET
        else:
            client_auth_method = self.client_auth_method

        scopes = self.scopes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if grant_type is not UNSET:
            field_dict["grantType"] = grant_type
        if client_auth_method is not UNSET:
            field_dict["clientAuthMethod"] = client_auth_method
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("clientId", UNSET)

        client_secret = d.pop("clientSecret", UNSET)

        _grant_type = d.pop("grantType", UNSET)
        grant_type: UpdateServerRequestOauthClientConfigurationType0GrantType | Unset
        if isinstance(_grant_type,  Unset):
            grant_type = UNSET
        else:
            grant_type = UpdateServerRequestOauthClientConfigurationType0GrantType(_grant_type)




        def _parse_client_auth_method(data: object) -> Literal['client_secret_basic'] | Literal['client_secret_post'] | Literal['none'] | str | Unset:
            if isinstance(data, Unset):
                return data
            client_auth_method_type_0 = cast(Literal['client_secret_basic'] , data)
            if client_auth_method_type_0 != 'client_secret_basic':
                raise ValueError(f"clientAuthMethod_type_0 must match const 'client_secret_basic', got '{client_auth_method_type_0}'")
            return client_auth_method_type_0
            client_auth_method_type_1 = cast(Literal['client_secret_post'] , data)
            if client_auth_method_type_1 != 'client_secret_post':
                raise ValueError(f"clientAuthMethod_type_1 must match const 'client_secret_post', got '{client_auth_method_type_1}'")
            return client_auth_method_type_1
            client_auth_method_type_2 = cast(Literal['none'] , data)
            if client_auth_method_type_2 != 'none':
                raise ValueError(f"clientAuthMethod_type_2 must match const 'none', got '{client_auth_method_type_2}'")
            return client_auth_method_type_2
            return cast(Literal['client_secret_basic'] | Literal['client_secret_post'] | Literal['none'] | str | Unset, data)

        client_auth_method = _parse_client_auth_method(d.pop("clientAuthMethod", UNSET))


        scopes = d.pop("scopes", UNSET)

        update_server_request_oauth_client_configuration_type_0 = cls(
            client_id=client_id,
            client_secret=client_secret,
            grant_type=grant_type,
            client_auth_method=client_auth_method,
            scopes=scopes,
        )


        update_server_request_oauth_client_configuration_type_0.additional_properties = d
        return update_server_request_oauth_client_configuration_type_0

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
