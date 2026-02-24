from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_server_request_oauth_metadata_type_0_as_type_0 import UpdateServerRequestOauthMetadataType0AsType0
  from ..models.update_server_request_oauth_metadata_type_0_resource_type_0 import UpdateServerRequestOauthMetadataType0ResourceType0





T = TypeVar("T", bound="UpdateServerRequestOauthMetadataType0")



@_attrs_define
class UpdateServerRequestOauthMetadataType0:
    """ 
        Attributes:
            requires_authorization (bool | Unset):
            resource (None | Unset | UpdateServerRequestOauthMetadataType0ResourceType0):
            as_ (None | Unset | UpdateServerRequestOauthMetadataType0AsType0):
     """

    requires_authorization: bool | Unset = UNSET
    resource: None | Unset | UpdateServerRequestOauthMetadataType0ResourceType0 = UNSET
    as_: None | Unset | UpdateServerRequestOauthMetadataType0AsType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_server_request_oauth_metadata_type_0_as_type_0 import UpdateServerRequestOauthMetadataType0AsType0
        from ..models.update_server_request_oauth_metadata_type_0_resource_type_0 import UpdateServerRequestOauthMetadataType0ResourceType0
        requires_authorization = self.requires_authorization

        resource: dict[str, Any] | None | Unset
        if isinstance(self.resource, Unset):
            resource = UNSET
        elif isinstance(self.resource, UpdateServerRequestOauthMetadataType0ResourceType0):
            resource = self.resource.to_dict()
        else:
            resource = self.resource

        as_: dict[str, Any] | None | Unset
        if isinstance(self.as_, Unset):
            as_ = UNSET
        elif isinstance(self.as_, UpdateServerRequestOauthMetadataType0AsType0):
            as_ = self.as_.to_dict()
        else:
            as_ = self.as_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if requires_authorization is not UNSET:
            field_dict["requiresAuthorization"] = requires_authorization
        if resource is not UNSET:
            field_dict["resource"] = resource
        if as_ is not UNSET:
            field_dict["as"] = as_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_server_request_oauth_metadata_type_0_as_type_0 import UpdateServerRequestOauthMetadataType0AsType0
        from ..models.update_server_request_oauth_metadata_type_0_resource_type_0 import UpdateServerRequestOauthMetadataType0ResourceType0
        d = dict(src_dict)
        requires_authorization = d.pop("requiresAuthorization", UNSET)

        def _parse_resource(data: object) -> None | Unset | UpdateServerRequestOauthMetadataType0ResourceType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resource_type_0 = UpdateServerRequestOauthMetadataType0ResourceType0.from_dict(data)



                return resource_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateServerRequestOauthMetadataType0ResourceType0, data)

        resource = _parse_resource(d.pop("resource", UNSET))


        def _parse_as_(data: object) -> None | Unset | UpdateServerRequestOauthMetadataType0AsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                as_type_0 = UpdateServerRequestOauthMetadataType0AsType0.from_dict(data)



                return as_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateServerRequestOauthMetadataType0AsType0, data)

        as_ = _parse_as_(d.pop("as", UNSET))


        update_server_request_oauth_metadata_type_0 = cls(
            requires_authorization=requires_authorization,
            resource=resource,
            as_=as_,
        )


        update_server_request_oauth_metadata_type_0.additional_properties = d
        return update_server_request_oauth_metadata_type_0

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
